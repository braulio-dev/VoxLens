import argparse
import os
from transcriber import Transcriber
from config import Config

if __name__ == "__main__":
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from src.transcriber import Transcriber
    from src.config import Config
    
    def main():
        parser = argparse.ArgumentParser(description="Audio Transcription using OpenAI Whisper")
        parser.add_argument("input_file", type=str, help="Path to input audio file")
        parser.add_argument("output_file", type=str, help="Path to the transcribed text")
        
        args = parser.parse_args()
        
        input_path = os.path.abspath(args.input_file)
        output_path = os.path.abspath(args.output_file)
        
        print(f"Processing file: {input_path}")
        transcriber = Transcriber(Config())
        transcription = transcriber.transcribe_audio(input_path)
        transcriber.save_transcription(transcription, output_path)
        
        print(f"Transcription saved to {output_path}")

    main()