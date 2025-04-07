import unittest
from src.utils.audio import load_audio, preprocess_audio
from src.utils.text import clean_text, tokenize_text

class TestUtils(unittest.TestCase):

    def test_load_audio(self):
        audio_path = 'data/raw/sample_audio.wav'
        audio_data = load_audio(audio_path)
        self.assertIsNotNone(audio_data)
        self.assertTrue(len(audio_data) > 0)

    def test_preprocess_audio(self):
        audio_data = [0.1, 0.2, 0.3, 0.4]  # Example audio data
        processed_audio = preprocess_audio(audio_data)
        self.assertIsNotNone(processed_audio)
        self.assertEqual(len(processed_audio), len(audio_data))

    def test_clean_text(self):
        raw_text = "This is a sample text! With punctuation."
        cleaned_text = clean_text(raw_text)
        self.assertEqual(cleaned_text, "This is a sample text with punctuation")

    def test_tokenize_text(self):
        text = "This is a sample text."
        tokens = tokenize_text(text)
        self.assertEqual(tokens, ["This", "is", "a", "sample", "text"])