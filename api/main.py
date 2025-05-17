from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import tempfile
import os
from transformers import WhisperForConditionalGeneration, WhisperProcessor
from transformers import pipeline
from fastapi.responses import StreamingResponse
from pydub import AudioSegment
import io

app = FastAPI(title="VoxLens API", description="API for speech recognition using Whisper model")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize transcription model and processor
model = WhisperForConditionalGeneration.from_pretrained("brauliodev/voxlens")
processor = WhisperProcessor.from_pretrained("brauliodev/voxlens")

model.generation_config.forced_decoder_ids = None

# Initialize transcription pipeline
pipe = pipeline(
    task="automatic-speech-recognition",
    model=model,
    processor=processor,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    device=0,
    chunk_length_s=30,
)

# Initialize summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def split_audio_chunks(audio_path, chunk_length_ms=5000):
    audio = AudioSegment.from_file(audio_path)
    for i in range(0, len(audio), chunk_length_ms):
        yield audio[i:i+chunk_length_ms]

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
        temp_path = temp_file.name  # Save the path

    # Now the file is closed, safe to use
    result = pipe(temp_path)
    os.unlink(temp_path)
    return {"text": result["text"]}

@app.post("/transcribe/stream")
async def transcribe_audio_stream(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
        content = await file.read()
        temp_file.write(content)
        temp_file.flush()
        temp_path = temp_file.name

    async def streamer():
        for idx, chunk in enumerate(split_audio_chunks(temp_path)):
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as chunk_file:
                chunk.export(chunk_file.name, format="wav")
                chunk_path = chunk_file.name  # Save the path

            # Now the file is closed, safe to use
            result = pipe(chunk_path)
            os.unlink(chunk_path)
            yield result["text"] + "\n"
        os.unlink(temp_path)

    return StreamingResponse(streamer(), media_type="text/plain")

@app.post("/summarize")
async def summarize(file: UploadFile = File(...), max_length: int = 130, min_length: int = 30):
    # Create a temporary file to store the uploaded audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
        content = await file.read()
        temp_file.write(content)
        temp_file.flush()
        temp_path = temp_file.name

    # First transcribe the audio
    transcription = pipe(temp_path)["text"]
    os.unlink(temp_path)
    
    # Then summarize the transcription
    if len(transcription.split()) < min_length:  # If text is too short, no need to summarize
        summary = transcription
    else:
        summary_result = summarizer(transcription, max_length=max_length, min_length=min_length, do_sample=False)
        summary = summary_result[0]['summary_text']
    
    return {
        "transcription": transcription,
        "summary": summary
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 