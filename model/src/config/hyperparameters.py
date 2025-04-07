# hyperparameters.py

class Hyperparameters:
    def __init__(self):
        self.learning_rate = 0.001
        self.batch_size = 32
        self.num_epochs = 10
        self.dropout_rate = 0.1
        self.weight_decay = 0.0001
        self.max_audio_length = 160000  # Example for 10 seconds of audio at 16kHz
        self.sample_rate = 16000
        self.num_layers = 6
        self.hidden_size = 512
        self.num_attention_heads = 8

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def display(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")