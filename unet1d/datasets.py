import torch
import pandas as pd
import os 

from torch import utils



class CSVDataset(utils.data.Dataset):

    def __init__(self, data_path: str, file_ext: str = ".csv", idx_col: str = "indexes") -> None:
        super().__init__()

        self.data = {
            dfile[:-len(file_ext)]: pd.read_csv(os.path.join(data_path, file_ext))
            for dfile in os.listdir(data_path)
            if dfile.endswith(file_ext) 
            and os.path.isfile(os.path.join(data_path, file_ext))
        }

        self.data_lens = {
            key: val[idx_col].max() 
            for key, val in self.data.items()
        }

    def __len__(self):
        pass

    def __getitem__(self, index):
        pass