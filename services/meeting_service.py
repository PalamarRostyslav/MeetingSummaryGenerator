"""
Meeting minutes generation service that orchestrates audio transcription and LLM generation
"""
from typing import Tuple
from services.audio_service import AudioTranscriptionService
from services.llm_service import LLMService

class MeetingMinutesService:
    """Service for generating meeting minutes from audio files"""
    
    def __init__(self):
        """Initialize the meeting minutes service"""
        self.audio_service = AudioTranscriptionService()
        self.llm_service = LLMService()
    
    def process_audio_file(self, audio_file_path: str) -> Tuple[str, str]:
        """
        Process an audio file and generate meeting minutes
        
        Args:
            audio_file_path: Path to the audio file
            
        Returns:
            Tuple of (transcription, meeting_minutes)
            
        Raises:
            Exception: If processing fails
        """
        try:
            # Step 1: Transcribe audio
            transcription = self.audio_service.transcribe_uploaded_file(audio_file_path)
            
            # Step 2: Generate meeting minutes
            meeting_minutes = self.llm_service.generate_minutes(transcription)
            
            return transcription, meeting_minutes
            
        except Exception as e:
            raise Exception(f"Meeting processing failed: {str(e)}")
    
    def process_transcription_only(self, transcription: str) -> str:
        """
        Generate meeting minutes from existing transcription
        
        Args:
            transcription: The meeting transcription text
            
        Returns:
            Generated meeting minutes
            
        Raises:
            Exception: If generation fails
        """
        try:
            return self.llm_service.generate_minutes(transcription)
        except Exception as e:
            raise Exception(f"Meeting minutes generation failed: {str(e)}")