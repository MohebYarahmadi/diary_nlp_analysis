from nltk.sentiment import SentimentIntensityAnalyzer
from pathlib import Path

# nltk.download('vader_lexicon')
# en_st_words = stopwords.words("english")

def read_files(path):
    with open(path, 'r') as file:
        return file.read()


def sentiment_analyzer(data):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(data)
    return score    # output: {'neg': 0.03, 'neu': 0.8, 'pos': 0.17, 'compound': 0.966}



def get_dates(filepath):
    dates = [Path(f).stem for f in filepath]
    dates.sort()
    return dates


if __name__ == "__main__":
    print("file read and analyse here")
