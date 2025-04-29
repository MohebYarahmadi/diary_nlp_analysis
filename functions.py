import re, nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

# nltk.download('vader_lexicon')
# en_st_words = stopwords.words("english")

def read_files(path):
    with open(path, 'r') as file:
        return file.read()


def word_list(data):
    pattern = re.compile("[a-zA-z]+")
    return re.findall(pattern, data)


def sentiment_analyzer(data):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(data)
    return score

if __name__ == "__main__":
    print("file read and analyse here")
