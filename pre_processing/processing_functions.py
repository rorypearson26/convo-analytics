"""Module for helper functions relating to processing."""
import regex as re

import pandas as pd
import numpy as np
import emoji


def process_datetime(df):
    df["datetime"] = pd.to_datetime(df["datetime"], format="%d/%m/%Y, %H:%M")
    df["hour"] = df["datetime"].dt.strftime("%H").astype("int64")
    return df


def add_stats(df):
    df["word_count"] = df["tokens"].str.len()
    df["letter_count"] = df["message"].apply(lambda s: len(s))
    df["avg_word_length"] = df["letter_count"] / df["word_count"]
    return df


def clean_sender(df, rename_dict):
    df["sender"] = df["sender"].str.replace(" - ", "")
    df["sender"].replace(to_replace=rename_dict, inplace=True)
    return df


def starts_with_timestamp(line):
    pattern = "\d{2}\/\d{2}\/\d{4}, \d{2}:\d{2} - "
    result = re.match(pattern, line)
    if result:
        return True
    return False


def remove_link_stats(df, word_length=18):
    df["avg_word_length"].where(
        df["avg_word_length"] < word_length, np.nan, inplace=True
    )
    return df


def extract_emojis(string):
    return [char for char in string if char in emoji.UNICODE_EMOJI]


def remove_media_stats(df, phrase="<Media omitted>"):
    df.loc[
        df["message"] == phrase, ["word_count", "letter_count", "avg_word_length"]
    ] = np.nan
    return df


def process_word_series(word_series):
    word_series.loc[word_series == "<Media omitted>"] = np.nan
    word_series.dropna(inplace=True)
    word_series = word_series.str.lower()
    words = " ".join(review for review in word_series)
    return words
