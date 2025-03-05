from whisper import load_model, DecodingOptions, decode
import os
from utils.audio_processor import AudioProcessor 

class Transcriber:
    def __init__(self, config):
        self.config = config
        self.audio_processor = AudioProcessor(config)

    def save_transcription(self, transcription, output_file_path):
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(transcription)

    def transcribe_audio(self, audio_file_path):
        # Path
        abs_path = os.path.abspath(audio_file_path)
        if not os.path.exists(abs_path):
            raise FileNotFoundError(f"Audio file not found: {abs_path}")
            
        # Preprocess Audio
        audio = self.audio_processor.load_audio(abs_path)
        audio, mel = self.audio_processor.preprocess_audio(audio)

        # Detect language
        model = load_model(self.config.model_name)
        _, probs = model.detect_language(mel)
        print(f"Detected language: {max(probs, key=probs.get)}")
        
        # Transcribe audio
        options = DecodingOptions()
        result = decode(model, mel, options) 

        return result.text