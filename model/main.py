from transformers import WhisperForConditionalGeneration, WhisperProcessor
from transformers import pipeline
import gradio as gr

model = WhisperForConditionalGeneration.from_pretrained("brauliodev/voxlens")
processor = WhisperProcessor.from_pretrained("brauliodev/voxlens")

model.generation_config.forced_decoder_ids = None

pipe = pipeline(
    task="automatic-speech-recognition",
    model=model,
    processor=processor,
    tokenizer=processor.tokenizer, # Explicitly pass the tokenizer
    feature_extractor=processor.feature_extractor, # Explicitly pass feature extractor
    device=0,
    chunk_length_s=30,
)

def transcribe(audio_filepath):
    result = pipe(audio_filepath)
    return result["text"]

print(transcribe("./model/test/test2.wav"))