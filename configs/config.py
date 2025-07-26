"""
Configuration settings for the Meeting Minutes Generator application.
"""
import os
from dataclasses import dataclass
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@dataclass
class Config:
    """Application configuration class."""
    
    # API Keys
    HUGGING_FACE_API_KEY: str = os.getenv("HUGGING_FACE_KEY")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    
    # Model configurations
    AUDIO_MODEL: str = "whisper-1"
    LLAMA_MODEL: str = "meta-llama/Meta-Llama-3.1-8B-Instruct"
    
    # Generation parameters
    MAX_NEW_TOKENS: int = 2000
    
    # System message for meeting minutes generation
    SYSTEM_MESSAGE: str = (
        "You are an assistant that produces minutes of meetings from transcripts, "
        "with summary, key discussion points, takeaways and action items with owners, "
        "in markdown format."
    )
    
    def validate(self) -> bool:
        """Validate that required API keys are present."""
        if not self.HUGGING_FACE_API_KEY:
            raise ValueError("HUGGING_FACE_KEY environment variable is required")
        if not self.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY environment variable is required")
        return True
    
# Global config instance
config = Config()