import whisper
import torch
import torchaudio

class WhisperModel:
    def __init__(self, hyperparameters):
        self.hyperparameters = hyperparameters
        self.model_size = "base"  # tiny, base, small, medium, large
        self.model = None
        self.load_model()

    def load_model(self):
        # Load the Whisper model
        self.model = whisper.load_model(self.model_size)
        return self.model

    def process_audio(self, audio_input):
        # Process the audio input for transcription
        # audio_input can be a path or an audio array
        return audio_input

    def transcribe(self, audio_input):
        # Generate text output from the audio input
        if self.model is None:
            self.load_model()
            
        if hasattr(audio_input, 'save'):
            # It's a file object from the API
            temp_path = "/tmp/audio_file.wav"
            audio_input.save(temp_path)
            audio_input = temp_path

        if isinstance(audio_input, torch.Tensor):
            # Resample to 16kHz and convert to mono
            sample_rate = 16000
            if audio_input.dim() > 1:  # Convert to mono if stereo
                audio_input = torch.mean(audio_input, dim=0, keepdim=True)
            audio_input = torchaudio.transforms.Resample(orig_freq=audio_input.size(1), new_freq=sample_rate)(audio_input)
            audio_input = audio_input.squeeze().numpy()

        result = self.model.transcribe(audio_input)
        return result['text']

    def tune_hyperparameters(self, new_hyperparameters):
        # Update hyperparameters and reload model if necessary
        self.hyperparameters.update(**new_hyperparameters)
        self.model = self.load_model()