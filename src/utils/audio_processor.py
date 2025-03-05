import numpy as np
import whisper

class AudioProcessor:
    def __init__(self, config=None):
        self.config = config
        self.sample_rate = config.sample_rate if config else 16000
    
    def load_audio(self, file_path):
        """Load audio file using Whisper's built-in audio loading function"""
        try:
            audio = whisper.load_audio(file_path)
            print(f"Successfully loaded audio from {file_path}")
            return audio
        except Exception as e:
            print(f"Error loading audio: {e}")
            raise

    def preprocess_audio(self, audio_data):
        """Preprocess audio for Whisper model"""
        audio = whisper.pad_or_trim(audio_data)
        mel = whisper.log_mel_spectrogram(audio).to(self.config.device)
        
        return audio, mel