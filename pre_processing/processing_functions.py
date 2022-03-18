"""Module for helper functions relating to processing."""
import pandas as pd
import regex as re


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
