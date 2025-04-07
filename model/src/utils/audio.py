def load_audio(file_path):
    import librosa
    audio, sample_rate = librosa.load(file_path, sr=None)
    return audio, sample_rate

def preprocess_audio(audio, target_sample_rate):
    import librosa
    if audio.shape[0] != target_sample_rate:
        audio = librosa.resample(audio, orig_sr=sample_rate, target_sr=target_sample_rate)
    return audio

def save_audio(file_path, audio, sample_rate):
    import soundfile as sf
    sf.write(file_path, audio, sample_rate)

def extract_features(audio):
    import numpy as np
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=13)
    return np.mean(mfccs.T, axis=0)