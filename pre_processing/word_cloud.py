"""Module to generate the chat wordcloud."""
from wordcloud import WordCloud, STOPWORDS

from processing_functions import process_word_series


class CloudyWords:
    def __init__(self, word_series, max_words=150, stop_words=None):
        self.stop_words = self.get_stop_words(stop_words)
        self.max_words = max_words
        self.words = process_word_series(word_series)
        self.wordcloud = self.get_wordcloud()

    def get_wordcloud(self):
        return WordCloud(
            min_word_length=2,
            max_words=150,
            stopwords=stop_words,
            relative_scaling=0.2,
            width=1200,
            height=1200,
            background_color="white",
        ).generate(words)

    @staticmethod
    def get_stop_words(stop_words):
        if stop_words:
            stop_words = stop_words + list(STOPWORDS)
        else:
            stop_words = list(STOPWORDS)
        return stop_words
