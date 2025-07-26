"""
Audio transcription service using OpenAI Whisper API
"""

from openai import OpenAI
from configs.config import config

class AudioTranscriptionService:
    """Service for transcribing audio files AI models"""
    
    def __init__(self):
        """Initialize the audio transcription service"""
        config.validate()
        self.client = OpenAI(api_key=config.OPENAI_API_KEY)
    
    def transcribe_audio(self, audio_file_path: str) -> str:
        """
        Transcribe an audio file to text
        
        Args:
            audio_file_path: Path to the audio file
            
        Returns:
            Transcribed text
            
        Raises:
            Exception: If transcription fails
        """
        try:
            with open(audio_file_path, "rb") as audio_file:
                transcription = self.client.audio.transcriptions.create(
                    model=config.AUDIO_MODEL,
                    file=audio_file,
                    response_format="text"
                )
                return transcription
        except Exception as e:
            raise Exception(f"Audio transcription failed: {str(e)}")
    
    def transcribe_uploaded_file(self, uploaded_file) -> str:
        """
        Transcribe an uploaded audio file from Gradio
        
        Args:
            uploaded_file: Gradio uploaded file object
            
        Returns:
            Transcribed text
            
        Raises:
            Exception: If transcription fails
        """
        if uploaded_file is None:
            raise Exception("No audio file provided")
        
        try:
            with open(uploaded_file, "rb") as audio_file:
                transcription = self.client.audio.transcriptions.create(
                    model=config.AUDIO_MODEL,
                    file=audio_file,
                    response_format="text"
                )
                return transcription
        except Exception as e:
            raise Exception(f"Audio transcription failed: {str(e)}")