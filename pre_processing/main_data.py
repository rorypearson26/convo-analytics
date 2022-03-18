"""Module for reading in raw text and performing basic processing."""
from pathlib import Path
import regex as re
import pandas as pd
import numpy as np


class RawData:
    def __init__(self, file_name, alias_dict):
        self.file_name = file_name
        self.alias_dict = alias_dict
        self.file_path = Path(__file__).parents[1] / "raw_export" / self.file_name
        self.cleaned_list = self.get_conversation_as_list()
        self.raw_series = pd.Series(self.cleaned_list)

    def get_conversation_as_list(self):
        cleaned_list = []
        with open(self.raw_file_path, encoding="utf-8") as f:
            message_buffer = []
            f.readline() # Skip first line as never a message.
            while True:
                line = f.readline() 
                if not line:
                    break
                line = line.strip()
                if self.starts_with_timestamp(line):
                    if message_buffer:
                        cleaned_list.append("\n".join(message_buffer))
                    message_buffer.clear()
                    message_buffer.append(line)
                else:
                    message_buffer.append(line)
        return cleaned_list
    
    @staticmethod
    def starts_with_timestamp(line):
        pattern = '\d{2}\/\d{2}\/\d{4}, \d{2}:\d{2} - '
        result = re.match(pattern, line)
        if result:
            return True
        return False


class ProcessedData:
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
    raw = ProcessedData("murphys_clan.txt")
    print("h")
