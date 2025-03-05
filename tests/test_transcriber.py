import unittest
from src.transcriber import Transcriber

class TestTranscriber(unittest.TestCase):

    def setUp(self):
        self.transcriber = Transcriber()

    def test_transcribe_audio(self):
        audio_file_path = 'audio/input/sample_audio.wav'
        transcription = self.transcriber.transcribe_audio(audio_file_path)
        self.assertIsInstance(transcription, str)
        self.assertGreater(len(transcription), 0)

    def test_save_transcription(self):
        transcription = "This is a test transcription."
        output_file_path = 'audio/output/test_transcription.txt'
        self.transcriber.save_transcription(transcription, output_file_path)

        with open(output_file_path, 'r') as file:
            saved_transcription = file.read()
        
        self.assertEqual(saved_transcription, transcription)

if __name__ == '__main__':
    unittest.main()