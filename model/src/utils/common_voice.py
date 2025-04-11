import os
import pandas as pd
from tqdm import tqdm
import torch
from torch.utils.data import Dataset

class CommonVoiceDataset(Dataset):
    """Common Voice dataset loader.
    
    This dataset loader handles the Common Voice format with TSV files
    and audio clips stored in the 'clips' directory.
    """
    
    def __init__(self, root_dir, tsv_file, transform=None):
        """
        Args:
            root_dir (str): Directory containing the 'clips' folder
            tsv_file (str): Path to the TSV file with metadata
            transform (callable, optional): Optional transform to be applied on audio
        """
        self.root_dir = root_dir
        self.clips_dir = os.path.join(root_dir, 'clips')
        self.data = pd.read_csv(tsv_file, sep='\t')
        self.transform = transform
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()
            
        # Get the file path and sentence
        file_name = self.data.iloc[idx]['path']
        sentence = self.data.iloc[idx]['sentence']
        
        # Load audio file
        audio_path = os.path.join(self.clips_dir, file_name)
        
        # You can use your existing audio loading utility here
        from src.utils.audio import load_audio
        audio, sample_rate = load_audio(audio_path)
        
        sample = {'audio': audio, 'text': sentence, 'path': audio_path}
        
        if self.transform:
            sample = self.transform(sample)
            
        return sample

def load_common_voice_dataset(root_dir, split='train'):
    """
    Load Common Voice dataset for a specific split
    
    Args:
        root_dir (str): Base directory containing Common Voice data
        split (str): One of 'train', 'dev', 'test'
        
    Returns:
        CommonVoiceDataset: Dataset instance for the specified split
    """
    tsv_file = os.path.join(root_dir, f'{split}.tsv')
    return CommonVoiceDataset(root_dir, tsv_file)

def process_common_voice_metadata(tsv_file, min_duration=1, max_duration=10):
    """
    Process Common Voice metadata and filter by duration
    
    Args:
        tsv_file (str): Path to TSV file
        min_duration (float): Minimum audio duration in seconds
        max_duration (float): Maximum audio duration in seconds
        
    Returns:
        pd.DataFrame: Filtered dataframe
    """
    df = pd.read_csv(tsv_file, sep='\t')
    
    # Filter by duration if 'duration' column exists
    if 'duration' in df.columns:
        df = df[(df['duration'] >= min_duration) & (df['duration'] <= max_duration)]
    
    return df
