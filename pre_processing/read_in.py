"""Module for reading in raw text and performing basic processing."""
from lib2to3.pgen2.pgen import DFAState
from pathlib import Path

import pandas as pd


class RawData:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_path = Path(__file__).parents[1] / "raw_export" / self.file_name
        self.raw_series = self.get_raw_series()
        self.df = self.process_dataframe()

    def get_raw_series(self):
        raw_lines = self.get_convo_as_list()
        raw_series = pd.Series(raw_lines)
        return raw_series

    def process_dataframe(self):
        df = pd.DataFrame()
        df[["date", "other"]] = self.raw_series.str.split("-", n=1, expand=True)
        df[["person", "message"]] = df["other"].str.split(":", n=1, expand=True)
        df.drop("other", inplace=True, axis=1)
        return df

    @staticmethod
    def split_columns(raw):
        

    def get_convo_as_list(self):
        with open(self.file_path, "r") as f:
            lines = f.read().splitlines()
        return lines


if __name__ == "__main__":
    raw = RawData("murphys_clan.txt")
    print("h")
