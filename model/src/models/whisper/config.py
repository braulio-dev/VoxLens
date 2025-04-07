class WhisperConfig:
    def __init__(self):
        self.model_name = "whisper"
        self.language = "en"
        self.sample_rate = 16000
        self.max_length = 512
        self.batch_size = 16
        self.learning_rate = 5e-5
        self.num_epochs = 3
        self.weight_decay = 0.01
        self.epsilon = 1e-8
        self.dropout_rate = 0.1

    def update_hyperparameters(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def display_config(self):
        config_dict = {k: v for k, v in self.__dict__.items()}
        for key, value in config_dict.items():
            print(f"{key}: {value}")