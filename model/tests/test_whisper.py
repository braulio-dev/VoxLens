import unittest
from src.models.whisper.model import WhisperModel
from src.models.whisper.tuner import HyperparameterTuner

class TestWhisperModel(unittest.TestCase):

    def setUp(self):
        self.model = WhisperModel()
        self.tuner = HyperparameterTuner()

    def test_model_loading(self):
        self.model.load_model()
        self.assertTrue(self.model.is_loaded)

    def test_audio_processing(self):
        audio_input = "path/to/test/audio.wav"
        text_output = self.model.process_audio(audio_input)
        self.assertIsInstance(text_output, str)

    def test_hyperparameter_tuning(self):
        initial_params = self.model.get_hyperparameters()
        new_params = self.tuner.tune_hyperparameters(initial_params)
        self.assertNotEqual(initial_params, new_params)

    def test_performance_metrics(self):
        audio_input = "path/to/test/audio.wav"
        self.model.load_model()
        text_output = self.model.process_audio(audio_input)
        metrics = self.model.evaluate_performance(text_output)
        self.assertGreater(metrics['accuracy'], 0.8)

if __name__ == '__main__':
    unittest.main()