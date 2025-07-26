"""
Large Language Model service for generating meeting minutes.
"""
import gc
import torch
from typing import List, Dict
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from huggingface_hub import login
from configs.config import config

class LLMService:
    """Service for generating meeting minutes using custom model"""
    
    def __init__(self):
        """Initialize the LLM service"""
        config.validate()
        login(config.HUGGING_FACE_API_KEY, add_to_git_credential=True)
        self._setup_quantization_config()
    
    def _setup_quantization_config(self):
        """Setup quantization configuration for efficient model loading"""
        self.quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_quant_type="nf4"
        )
    
    def generate_minutes(self, transcription: str) -> str:
        """
        Generate meeting minutes from transcription
        
        Args:
            transcription: The audio transcription text
            
        Returns:
            Generated meeting minutes in markdown format
            
        Raises:
            Exception: If generation fails
        """
        try:
            messages = self._prepare_messages(transcription)
            return self._generate_response(messages)
        except Exception as e:
            raise Exception(f"Meeting minutes generation failed: {str(e)}")
    
    def _prepare_messages(self, transcription: str) -> List[Dict[str, str]]:
        """
        Prepare messages for the LLM
        
        Args:
            transcription: The audio transcription text
            
        Returns:
            List of messages formatted for the LLM
        """
        user_prompt = (
            f"Below is an extract transcript of a meeting. Please write minutes in markdown, "
            f"including a summary with attendees, location and date; discussion points; "
            f"takeaways; and action items with owners.\n\n{transcription}"
        )
        
        return [
            {"role": "system", "content": config.SYSTEM_MESSAGE},
            {"role": "user", "content": user_prompt}
        ]
    
    def _generate_response(self, messages: List[Dict[str, str]]) -> str:
        """
        Generate response using the LLaMA model
        
        Args:
            messages: List of messages for the model
            
        Returns:
            Generated response text
        """
        tokenizer = None
        model = None
        
        try:
            # Load tokenizer
            tokenizer = AutoTokenizer.from_pretrained(config.LLAMA_MODEL)
            tokenizer.pad_token = tokenizer.eos_token
            
            # Prepare inputs
            inputs = tokenizer.apply_chat_template(
                messages, 
                return_tensors="pt"
            ).to("cuda")
            
            # Load model
            model = AutoModelForCausalLM.from_pretrained(
                config.LLAMA_MODEL,
                device_map="auto",
                quantization_config=self.quant_config
            )
            
            # Generate response
            with torch.no_grad():
                outputs = model.generate(
                    inputs,
                    max_new_tokens=config.MAX_NEW_TOKENS,
                    do_sample=True,
                    temperature=0.7,
                    pad_token_id=tokenizer.eos_token_id
                )
            
            # Decode response
            response = tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # Extract only the generated part (remove the input prompt)
            # Find the assistant's response part
            if "assistant" in response:
                response_parts = response.split("assistant")
                if len(response_parts) > 1:
                    response = response_parts[-1].strip()
            
            return response
            
        finally:
            # Clean up memory
            if model is not None:
                del model
            if tokenizer is not None:
                del tokenizer
            if 'inputs' in locals():
                del inputs
            if 'outputs' in locals():
                del outputs
            
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()