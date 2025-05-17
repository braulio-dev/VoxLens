

# VoxLens 🎙️ Voice to Text Summarizer

VoxLens is a voice transcription and summarization tool that converts spoken audio into text and provides concise summaries. Perfect for meetings, lectures, or any scenario where you need quick summaries of voice recordings.

## About This Project

VoxLens was developed as a final project for the Deep Learning course in the 6th semester at CETYS Universidad for Expo Ingeniería. Our team wanted to create a practical application of speech recognition and natural language processing that could be useful in everyday scenarios.

We spent countless late nights training models, debugging API calls, and tweaking the UI - fueled by coffee and the occasional pizza. But honestly, seeing it all come together was worth every debugging session!

## Features

- **Voice Transcription**: Accurate speech-to-text conversion
- **Automatic Summarization**: Get concise summaries of your recordings
- **Real-time Processing**: Quick results without long waits
- **Simple Interface**: Just hit record and let VoxLens do the rest
- **Dark/Light Mode**: Easy on the eyes, day or night
- **Multi-language Support**: Currently supports English and Spanish UI

## Tech Stack

- **Frontend**: Vue.js with TypeScript
- **Backend**: FastAPI
- **ML Models**: Whisper for transcription, BART for summarization
- **Deployment**: Docker for containerization

## Getting Started

### Prerequisites

- Node.js (v14+)
- Python 3.8+
- Docker (optional, for containerized deployment)

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/braulio-dev/VoxLens.git
   cd VoxLens
   ```

2. Set up the API
   ```bash
   cd api
   pip install -r requirements.txt
   python main.py
   ```

3. Set up the web app
   ```bash
   cd web-app
   npm install
   npm run dev
   ```

4. Open your browser and navigate to `http://localhost:5173`

## Project Structure

- `/api` - FastAPI backend for transcription and summarization
- `/model` - ML model training and evaluation code
- `/web-app` - Vue.js frontend application

## Team

- [Braulio Chamerry](https://github.com/braulio-dev)
- [Renata Sánchez](https://github.com/RenataSz4)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.