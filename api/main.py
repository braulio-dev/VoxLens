from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import tempfile
import os
from transformers import WhisperForConditionalGeneration, WhisperProcessor
from transformers import pipeline

app = FastAPI(title="VoxLens API", description="API for speech recognition using Whisper model")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize model and processor
model = WhisperForConditionalGeneration.from_pretrained("brauliodev/voxlens")
processor = WhisperProcessor.from_pretrained("brauliodev/voxlens")

model.generation_config.forced_decoder_ids = None

# Initialize pipeline
pipe = pipeline(
    task="automatic-speech-recognition",
    model=model,
    processor=processor,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    device=0,
    chunk_length_s=30,
)

@app.get("/")
async def root():
    return {"message": "Welcome to VoxLens API"}

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    # Create a temporary file to store the uploaded audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
        content = await file.read()
        temp_file.write(content)
        temp_file.flush()
        
        # Transcribe the audio
        result = pipe(temp_file.name)
        
        # Clean up the temporary file
        os.unlink(temp_file.name)
        
        return {"text": result["text"]} 