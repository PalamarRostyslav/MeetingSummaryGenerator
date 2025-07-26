"""
Gradio user interface for the Meeting Minutes Generator
"""
import gradio as gr
from typing import Tuple
from services.meeting_service import MeetingMinutesService

class MeetingMinutesUI:
    """Gradio UI for meeting minutes generation"""
    
    def __init__(self):
        """Initialize the UI with meeting service"""
        self.meeting_service = MeetingMinutesService()
    
    def process_audio_upload(self, audio_file) -> Tuple[str, str, str]:
        """
        Process uploaded audio file and return results
        
        Args:
            audio_file: Uploaded audio file from Gradio
            
        Returns:
            Tuple of (status_message, transcription, meeting_minutes)
        """
        if audio_file is None:
            return "❌ Please upload an audio file.", "", ""
        
        try:
            # Update status
            status = "🔄 Processing audio file..."
            
            # Process the audio file
            transcription, meeting_minutes = self.meeting_service.process_audio_file(audio_file)
            
            return "✅ Processing completed successfully!", transcription, meeting_minutes
            
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            return error_msg, "", ""
    
    def process_text_input(self, transcription_text: str) -> Tuple[str, str]:
        """
        Process transcription text and generate meeting minutes
        
        Args:
            transcription_text: Meeting transcription text
            
        Returns:
            Tuple of (status_message, meeting_minutes)
        """
        if not transcription_text.strip():
            return "❌ Please enter transcription text.", ""
        
        try:
            meeting_minutes = self.meeting_service.process_transcription_only(transcription_text)
            return "✅ Meeting minutes generated successfully!", meeting_minutes
            
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            return error_msg, ""
    
    def create_interface(self) -> gr.Blocks:
        """
        Create and return the Gradio interface
        
        Returns:
            Gradio Blocks interface
        """
        with gr.Blocks(
            title="Meeting Minutes Generator",
            theme=gr.themes.Soft(),
            css="""
            .status-success { color: #10b981 !important; }
            .status-error { color: #ef4444 !important; }
            .status-processing { color: #f59e0b !important; }
            """
        ) as interface:
            # Header
            gr.Markdown(
                """
                # 🎙️ Meeting Minutes Generator
                
                Transform your meeting recordings into professional minutes with AI-powered transcription and summarization.
                """
            )
            
            with gr.Tabs():
                
                # Tab 1: Audio Upload
                with gr.Tab("🎵 Audio to Minutes", id="audio_tab"):
                    gr.Markdown("### Upload an audio file to generate meeting minutes")
                    
                    with gr.Row():
                        with gr.Column(scale=1):
                            audio_input = gr.Audio(
                                label="📁 Upload Meeting Audio",
                                type="filepath",
                                format="mp3"
                            )
                            
                            process_audio_btn = gr.Button(
                                "🚀 Generate Minutes from Audio",
                                variant="primary",
                                size="lg"
                            )
                    
                    # Status and results
                    audio_status = gr.Markdown("", elem_classes=["status-message"])
                    
                    with gr.Row():
                        with gr.Column():
                            transcription_output = gr.Textbox(
                                label="📝 Transcription",
                                lines=8,
                                max_lines=15,
                                interactive=False,
                                placeholder="Audio transcription will appear here..."
                            )
                        
                        with gr.Column():
                            minutes_output = gr.Markdown(
                                label="📋 Meeting Minutes",
                                value="Meeting minutes will appear here...",
                            )
                
                # Tab 2: Text Input
                with gr.Tab("📝 Text to Minutes", id="text_tab"):
                    gr.Markdown("### Enter transcription text to generate meeting minutes")
                    
                    transcription_input = gr.Textbox(
                        label="📄 Meeting Transcription",
                        lines=10,
                        max_lines=20,
                        placeholder="Paste your meeting transcription here..."
                    )
                    
                    process_text_btn = gr.Button(
                        "🚀 Generate Minutes from Text",
                        variant="primary",
                        size="lg"
                    )
                    
                    text_status = gr.Markdown("", elem_classes=["status-message"])
                    text_minutes_output = gr.Markdown(
                        label="📋 Meeting Minutes",
                        value="Meeting minutes will appear here..."
                    )
            
            # Examples section
            with gr.Accordion("💡 Tips & Examples", open=False):
                gr.Markdown(
                    """
                    ### Audio Requirements:
                    - Supported formats: MP3, WAV, M4A, FLAC
                    - Maximum file size: 25MB
                    - Clear audio quality recommended for best results
                    
                    ### What You'll Get:
                    - **Summary** with attendees, location, and date
                    - **Key Discussion Points** organized by topic
                    - **Takeaways** and decisions made
                    - **Action Items** with assigned owners
                    
                    ### Example Output:
                    ```markdown
                    # Meeting Minutes - Project Planning Session
                    
                    ## Summary
                    - **Date:** January 15, 2024
                    - **Attendees:** John Smith, Sarah Johnson, Mike Chen
                    - **Location:** Conference Room A
                    
                    ## Discussion Points
                    - Project timeline and milestones
                    - Budget allocation and resources
                    
                    ## Action Items
                    - [ ] Finalize project scope - John Smith (Due: Jan 20)
                    - [ ] Prepare budget proposal - Sarah Johnson (Due: Jan 22)
                    ```
                    """
                )
            
            # Event handlers
            process_audio_btn.click(
                fn=self.process_audio_upload,
                inputs=[audio_input],
                outputs=[audio_status, transcription_output, minutes_output],
                show_progress=True
            )
            
            process_text_btn.click(
                fn=self.process_text_input,
                inputs=[transcription_input],
                outputs=[text_status, text_minutes_output],
                show_progress=True
            )
        
        return interface
    
    def launch(self, **kwargs):
        """
        Launch the Gradio interface
        
        Args:
            **kwargs: Additional arguments for gr.Interface.launch()
        """
        interface = self.create_interface()
        interface.launch(**kwargs)


# Create UI instance for easy importing
meeting_ui = MeetingMinutesUI()