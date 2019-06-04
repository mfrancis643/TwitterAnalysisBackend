from django.http import HttpResponse
import json


class TwitterHttpResponse:
    score = ''
    tweets = []

    def __init__(self, parScore, parTweets):
        self.tweets = parTweets
        self.score = parScore

    def getScore(self):
        return self.score

    def getResponse(self):
        response = [{
            'score': self.score
        }]
        return response

    def getTweets(self):
        return self.tweets

    def build(self):
        data = {}
        data['score'] = self.getScore()
        data['tweets'] = self.getTweets()
        jsonBody = json.dumps(data)

        response = HttpResponse(jsonBody)
        return response
