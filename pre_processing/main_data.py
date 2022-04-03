"""Module for reading in raw text and performing basic processing."""
from pathlib import Path
import regex as re

import pandas as pd
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English

from pre_processing.processing_functions import (
    process_datetime,
    add_stats,
    clean_sender,
    starts_with_timestamp,
    extract_emojis,
    remove_link_stats,
    remove_media_stats,
)

nlp = English()
tokenizer = Tokenizer(nlp.vocab)


class RawData:
    def __init__(self, raw_text, alias_dict={}):
        self.raw_text = raw_text
        self.alias_dict = alias_dict
        self.cleaned_list = self.get_conversation_as_list()
        self.series = pd.Series(self.cleaned_list)

    def get_conversation_as_list(self):
        cleaned_list = []
        f = self.raw_text
        # with open(self.raw_text) as f:
        message_buffer = []
        f.readline()  # Skip first line as never a message.
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            if starts_with_timestamp(line):
                if message_buffer:
                    cleaned_list.append("\n".join(message_buffer))
                message_buffer.clear()
                message_buffer.append(line)
            else:
                message_buffer.append(line)
        return cleaned_list


class ProcessedData:
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.df = self.process_dataframe()
        self.df_filtered = self.df.copy()
        self.df_emoji = self.process_emoji_dataframe()

    def process_dataframe(self):
        df = self.raw_data.series.str.extract(
            "(\d{2}\/\d{2}\/\d{4}, \d{2}:\d{2})?( - .*|.*)"
        )
        df.rename(columns={0: "datetime", 1: "other"}, inplace=True)
        df = process_datetime(df)
        df[["sender", "message"]] = df["other"].str.split(": ", n=1, expand=True)
        df.drop("other", inplace=True, axis=1)
        df.dropna(inplace=True)
        clean_sender(df=df, rename_dict=self.raw_data.alias_dict)
        df["tokens"] = df.message.apply(lambda x: tokenizer(x))
        df = add_stats(df)
        df = remove_link_stats(df)
        df = remove_media_stats(df)
        return df

    def process_emoji_dataframe(self):
        df = self.df.copy()
        df["emoji"] = df.message.apply(extract_emojis)
        df.drop(["message", "tokens"], axis=1, inplace=True)
        df = df.explode("emoji")
        return df
