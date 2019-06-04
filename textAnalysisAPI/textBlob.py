from textblob import TextBlob
import nltk
nltk.download('punkt')


class TextAnalysis:
    wiki = []

    def __init__(self, tweet):
        self.populateWiki(tweet)

    def populateWiki(self, tweet):
        self.wiki = TextBlob(tweet)

    def analyseTweet(self):
        sent = self.wiki.sentiment
        pol = sent.polarity
        score = self.scaleScore(pol)
        print("score:     " + str(score) + "\n")
        return score

    def scaleScore(self, parPol):
        return ((parPol + 1) / 2) * 10
