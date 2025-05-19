# model/src/utils/metrics.py
import numpy as np
from transformers import WhisperForConditionalGeneration, WhisperProcessor
import torch
import re
import Levenshtein

class SpeechRecognitionMetrics:
    def __init__(self, model_path="brauliodev/voxlens"):
        self.model = WhisperForConditionalGeneration.from_pretrained(model_path)
        self.model.generation_config.forced_decoder_ids = None
        self.processor = WhisperProcessor.from_pretrained(model_path)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)
        self.model.eval()
    
    def transcribe(self, audio_path):
        """Transcribe audio file using the model"""
        from transformers import pipeline
        pipe = pipeline(
            task="automatic-speech-recognition",
            model=self.model,
            processor=self.processor,
            tokenizer=self.processor.tokenizer,
            feature_extractor=self.processor.feature_extractor,
            device=0 if self.device == "cuda" else -1,
        )
        result = pipe(audio_path)
        return result["text"]
    
    def character_error_rate(self, reference, hypothesis):
        """Calculate Character Error Rate (CER)"""
        if len(reference) == 0:
            return 1.0 if len(hypothesis) > 0 else 0.0
        
        edit_distance = Levenshtein.distance(reference, hypothesis)
        return edit_distance / len(reference)
    
    def word_error_rate(self, reference, hypothesis):
        """Calculate Word Error Rate (WER)"""
        ref_words = reference.lower().split()
        hyp_words = hypothesis.lower().split()
        
        if len(ref_words) == 0:
            return 1.0 if len(hyp_words) > 0 else 0.0
        
        # Calculate edit distance on word level
        edit_distance = Levenshtein.distance(ref_words, hyp_words)
        return edit_distance / len(ref_words)
    
    def word_accuracy(self, reference, hypothesis):
        """Calculate Word Accuracy (1 - WER)"""
        wer = self.word_error_rate(reference, hypothesis)
        return 1.0 - wer
    
    def character_accuracy(self, reference, hypothesis):
        """Calculate Character Accuracy (1 - CER)"""
        cer = self.character_error_rate(reference, hypothesis)
        return 1.0 - cer
    
    def levenshtein_distance(self, reference, hypothesis):
        """Calculate raw Levenshtein distance"""
        return Levenshtein.distance(reference, hypothesis)
    
    def evaluate(self, audio_paths, reference_texts):
        """
        Evaluate the model on multiple audio files
        
        Args:
            audio_paths: List of paths to audio files
            reference_texts: List of reference transcriptions
            
        Returns:
            Dictionary of average metrics
        """
        results = {
            "character_accuracy": [],
            "word_accuracy": [],
            "levenshtein_distance": []
        }
        
        for audio_path, reference in zip(audio_paths, reference_texts):
            hypothesis = self.transcribe(audio_path)
            hypothesis = re.sub(r'\.(?!\s)', '. ', hypothesis)
            
            # Calculate metrics
            results["character_accuracy"].append(
                self.character_accuracy(reference, hypothesis)
            )
            results["word_accuracy"].append(
                self.word_accuracy(reference, hypothesis)
            )
            results["levenshtein_distance"].append(
                self.levenshtein_distance(reference, hypothesis)
            )
            
            # Print individual results
            print(f"Audio: {audio_path}")
            print(f"Reference: {reference}")
            print(f"Hypothesis: {hypothesis}")
            print(f"Character Accuracy: {results['character_accuracy'][-1]:.4f}")
            print(f"Word Accuracy: {results['word_accuracy'][-1]:.4f}")
            print(f"Levenshtein Distance: {results['levenshtein_distance'][-1]}")
            print("-" * 50)
        
        # Calculate averages
        avg_results = {
            "avg_character_accuracy": np.mean(results["character_accuracy"]),
            "avg_word_accuracy": np.mean(results["word_accuracy"]),
            "avg_levenshtein_distance": np.mean(results["levenshtein_distance"])
        }
        
        return {**results, **avg_results}

# Example usage
if __name__ == "__main__":
    # Initialize metrics calculator
    metrics = SpeechRecognitionMetrics()
    
    # Example data - replace with your test data
    audio_paths = [
        "A:/Projects/VoxLens/model/test/test2.wav"
    ]
    reference_texts = [
        "Una niña encontró una llave dorada enterrada en su jardín. Al usarla en un viejo ropero, descubrió un mundo donde los animales hablaban y el tiempo corría al revés. Decidió quedarse allí un rato, prometiendo regresar antes de que su gato notara su ausencia.",
    ]
    
    # Evaluate and print results
    evaluation_results = metrics.evaluate(audio_paths, reference_texts)
    
    print("\nAVERAGE RESULTS:")
    print(f"Average Character Accuracy: {evaluation_results['avg_character_accuracy']:.4f}")
    print(f"Average Word Accuracy: {evaluation_results['avg_word_accuracy']:.4f}")
    print(f"Average Levenshtein Distance: {evaluation_results['avg_levenshtein_distance']:.2f}")