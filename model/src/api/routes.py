from flask import Flask, request, jsonify
from src.models.whisper.model import WhisperModel
from src.models.summarizer.model import SummarizerModel
from src.config.hyperparameters import Hyperparameters

app = Flask(__name__)

whisper_model = WhisperModel(Hyperparameters)
summarizer_model = SummarizerModel()

@app.route('/api/transcribe', methods=['POST'])
def transcribe_audio():
    audio_file = request.files['audio']
    transcription = whisper_model.transcribe(audio_file)
    return jsonify({'transcription': transcription})

@app.route('/api/summarize', methods=['POST'])
def summarize_text():
    text = request.json['text']
    summary = summarizer_model.summarize(text)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)