# 🎙️ Meeting Minutes Generator

An AI-powered application that automatically transcribes meeting audio files and generates professional meeting minutes using OpenAI's Whisper and Meta's LLaMA models.

## ✨ Features

- 🎵 **Audio Transcription**: Convert meeting recordings to text using OpenAI Whisper
- 📝 **Smart Summarization**: Generate structured meeting minutes with LLaMA
- 🎨 **Modern UI**: Clean, intuitive Gradio interface with dual input methods
- ⚡ **GPU Optimization**: Efficient memory usage with 4-bit quantization
- 📋 **Professional Output**: Structured minutes with summaries, action items, and owners
- 🌐 **Web Interface**: Easy-to-use browser-based interface

## 📋 Generated Minutes Include

- **Summary** with attendees, location, and date
- **Key Discussion Points** organized by topic  
- **Takeaways** and decisions made
- **Action Items** with assigned owners and due dates
- Professional markdown formatting ready for documentation

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- CUDA-compatible GPU (recommended for faster processing)
- OpenAI API key
- Hugging Face account and token

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/meeting-minutes-generator.git
   cd meeting-minutes-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   HUGGING_FACE_KEY=your_hugging_face_token_here
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

5. **Open your browser**
   
   Navigate to `http://localhost:7999` to access the interface.

## 🏗️ Project Structure

```
meeting-minutes-generator/
├── main.py                # Application entry point
├── configs/        
│   ├── config.py          # Configuration settings
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── .gitignore             # Git ignore rules
├── README.md              # This file
├── services/
│   ├── __init__.py
│   ├── audio_service.py   # Audio transcription service
│   ├── llm_service.py     # LLM text generation service
│   └── meeting_service.py # Main orchestration service
└── ui/
    ├── __init__.py
    └── gradio_interface.py # Gradio UI components
```

## 🎯 Usage

### Method 1: Audio Upload
1. Navigate to the "🎵 Audio to Minutes" tab
2. Upload your meeting audio file (MP3, WAV, M4A, FLAC)
3. Click "🚀 Generate Minutes from Audio"
4. View transcription and generated minutes side by side

### Method 2: Text Input
1. Navigate to the "📝 Text to Minutes" tab  
2. Paste your existing meeting transcription
3. Click "🚀 Generate Minutes from Text"
4. View professionally formatted minutes

## ⚙️ Configuration

### Audio Requirements
- **Supported formats**: MP3, WAV, M4A, FLAC
- **Maximum file size**: 25MB  
- **Quality**: Clear audio recommended for best transcription results

### Model Configuration
- **Audio Model**: OpenAI Whisper (`whisper-1`)
- **Text Model**: Meta LLaMA 3.1 8B Instruct
- **Quantization**: 4-bit quantization for memory efficiency
- **Max Tokens**: 2000 tokens for comprehensive minutes

### Example Output

```markdown
# Meeting Minutes - Project Planning Session

## Summary
- **Date:** January 15, 2024
- **Time:** 2:00 PM - 3:30 PM
- **Location:** Conference Room A
- **Attendees:** John Smith (Project Manager), Sarah Johnson (Developer), Mike Chen (Designer)

## Discussion Points

### Project Timeline
- Discussed Q1 deliverables and milestone dates
- Reviewed resource allocation for upcoming sprints
- Identified potential blockers in development phase

### Budget and Resources
- Approved additional budget for external contractor
- Discussed team expansion plans for Q2
- Reviewed current tool and software requirements

## Key Takeaways
- Project is on track for Q1 delivery
- Need to hire additional developer by February
- Client feedback integration will require 2-week buffer

## Action Items
- [ ] Finalize project scope document - John Smith (Due: Jan 20)
- [ ] Prepare budget proposal for Q2 expansion - Sarah Johnson (Due: Jan 22)
- [ ] Create mockups for client review - Mike Chen (Due: Jan 25)
- [ ] Schedule follow-up meeting with stakeholders - John Smith (Due: Jan 18)
```

## 🔧 Advanced Configuration

### Custom Models
Edit `config.py` to use different models:

```python
class Config:
    AUDIO_MODEL = "whisper-1"  # OpenAI Whisper model
    LLAMA_MODEL = "meta-llama/Meta-Llama-3.1-8B-Instruct"  # LLaMA model
    MAX_NEW_TOKENS = 2000  # Adjust response length
```

### Custom System Prompts
Modify the AI behavior by editing `SYSTEM_MESSAGE` in `config.py`:

```python
SYSTEM_MESSAGE = "Your custom instructions for meeting minute generation..."
```

### Server Configuration
Adjust server settings in `main.py`:

```python
meeting_ui.launch(
    server_name="127.0.0.1",  # Server address
    server_port=7999,         # Port number
    share=True,               # Create public link
    inbrowser=True           # Auto-open browser
)
```

## 🐛 Troubleshooting

### Error Messages Guide
- ❌ **Red status**: Check console for detailed error information
- ✅ **Green status**: Processing completed successfully
- 🔄 **Yellow status**: Processing in progress - please wait

### Performance Tips
- Use GPU for faster processing (CUDA required)
- Ensure stable internet connection for API calls
- Close other GPU-intensive applications
- Use shorter audio files (<10 minutes) for faster processing

## 🔒 Security & Privacy

- API keys are stored locally in `.env` file
- Audio files are processed locally and sent only to OpenAI for transcription
- No data is stored on external servers beyond API calls
- Generated minutes remain on your local machine

- **Backend**: Python, Transformers, PyTorch
- **Frontend**: Gradio
- **AI Models**: OpenAI Whisper, Meta LLaMA
- **APIs**: OpenAI API, Hugging Face Hub
- **Optimization**: BitsAndBytesConfig (4-bit quantization)


## 🔮 Roadmap

- [ ] Support for multiple languages
- [ ] Batch processing for multiple files
- [ ] Custom templates for different meeting types
- [ ] Integration with calendar applications
- [ ] Export to various formats (PDF, Word, etc.)
- [ ] Real-time transcription during live meetings

---
