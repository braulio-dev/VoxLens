from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

def evaluate_whisper_model(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted')
    recall = recall_score(y_true, y_pred, average='weighted')
    f1 = f1_score(y_true, y_pred, average='weighted')
    
    metrics = {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1
    }
    
    return metrics

def evaluate_summarizer_model(y_true, y_pred):
    # Placeholder for summarizer evaluation metrics
    # Future implementation will include specific metrics for summarization
    return {
        'summary_quality': 'To be implemented'
    }