"""Module for reading in raw text and performing basic processing."""
from pathlib import Path

import pandas as pd


class RawData:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_path = Path(__file__).parents[1] / "raw_export" / self.file_name
        self.df = self.get_raw_dataframe()
        pass

    def get_raw_dataframe(self):
        df = pd.read_csv(self.file_path)
        return df


if __name__ == "__main__":
    raw = RawData("murphys_clan.txt")
    print("h")
