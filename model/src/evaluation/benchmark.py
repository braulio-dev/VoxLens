def benchmark_model(model, test_data, metrics):
    results = {}
    
    for metric in metrics:
        if metric == 'accuracy':
            results[metric] = evaluate_accuracy(model, test_data)
        elif metric == 'latency':
            results[metric] = evaluate_latency(model, test_data)
        elif metric == 'throughput':
            results[metric] = evaluate_throughput(model, test_data)
    
    return results

def evaluate_accuracy(model, test_data):
    correct_predictions = 0
    total_predictions = len(test_data)

    for audio, expected_text in test_data:
        predicted_text = model.transcribe(audio)
        if predicted_text == expected_text:
            correct_predictions += 1

    return correct_predictions / total_predictions

def evaluate_latency(model, test_data):
    import time
    latencies = []

    for audio in test_data:
        start_time = time.time()
        model.transcribe(audio)
        latencies.append(time.time() - start_time)

    return sum(latencies) / len(latencies)

def evaluate_throughput(model, test_data):
    import time
    start_time = time.time()

    for audio in test_data:
        model.transcribe(audio)

    return len(test_data) / (time.time() - start_time)