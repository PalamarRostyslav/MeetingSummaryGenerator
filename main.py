"""
Main application entry point for the Meeting Minutes Generator
"""
import sys
import os
from ui.gradio_interface import meeting_ui

# Add the current directory to Python path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    """Main function to launch the application"""
    try:
        print("🚀 Starting Meeting Minutes Generator...")
        print("📝 Loading AI models and services...")
        
        # Launch the Gradio interface
        meeting_ui.launch(
            server_name="0.0.0.0",
            server_port=7999,
            share=False, 
            debug=False,  
            show_error=True,  
            quiet=False
        )
        
    except KeyboardInterrupt:
        print("\n⏹️ Application stopped by user.")
    except Exception as e:
        print(f"❌ Error starting application: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()