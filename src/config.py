import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent.parent / '.env'
example_path = Path(__file__).parent.parent / '.env.example'

if env_path.exists():
    load_dotenv(dotenv_path=env_path)
elif example_path.exists():
    load_dotenv(dotenv_path=example_path)
else:
    print("Warning: No .env or .env.example file found. Using defaults.")

class Config:
    def __init__(self):
        self.output_format = os.getenv('OUTPUT_FORMAT', 'txt')
        self.model_name = os.getenv('MODEL_NAME', 'base')
        self.sample_rate = int(os.getenv('SAMPLE_RATE', 16000))
        self.max_length = int(os.getenv('MAX_LENGTH', 300)) if os.getenv('MAX_LENGTH') else None
        self.output_dir = os.getenv('OUTPUT_DIR', 'audio/output')
        self.input_dir = os.getenv('INPUT_DIR', 'audio/input')
        self.device = os.getenv('DEVICE', 'cpu')