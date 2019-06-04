import oauth2 as oauth
import json


class TwitterApi:

    def getUrlPrefixProfile(self, twitterHandle):
        return "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=" + twitterHandle + "&count=50"

    def getUrlPrefixTweet(self, tweetId):
        return "https://api.twitter.com/1.1/statuses/show.json?id=" + str(tweetId)

    def getUrlPrefixSearch(self, twitterHandle):
        return "https://api.twitter.com/1.1/search/tweets.json?q=" + twitterHandle + "&result_type=mixed&count=100"

    def getClient(self):
        consumerKey = ""
        consumerSecret = ""
        accessToken = ""
        accessSecret = ""

        consumer = oauth.Consumer(key=consumerKey, secret=consumerSecret)
        accessToken = oauth.Token(key=accessToken, secret=accessSecret)
        client = oauth.Client(consumer, accessToken)
        return client

    def getTimeline(self, twitterHandle):
        client = self.getClient()
        response, data = client.request(self.getUrlPrefixProfile(twitterHandle))
        if response.status != 200:
            if response.status == 404:
                errorMessage = "Twitter Handle Not Found"
            else:
                errorMessage = "Something Went Wrong"
            return errorMessage
        formatted = json.loads(data.decode('latin1'))
        tweets = []
        for tweet in formatted:
            tweets.append(tweet['text'])
            #print(tweet['text'])
        return tweets

    def getAuthor(self, tweetId):
        client = self.getClient()
        response, data = client.request(self.getUrlPrefixTweet(tweetId))
        print(str(data))
        if response.status != 200:
            if response.status == 404:
                errorMessage = "Tweet ID Handle Not Found"
            else:
                errorMessage = "Something Went Wrong"
            return errorMessage
        formatted = json.loads(data.decode('latin1'))
        author = formatted['user']['screen_name']
        return author

    def getStatuses(self, author, tweetId):
        client = self.getClient()
        response, data = client.request(self.getUrlPrefixSearch(author))
        if response.status != 200:
            print(response.status)
        formatted = json.loads(data.decode('latin1'))
        formatted = formatted['statuses']
        statuses = []
        for status in formatted:
            print("STATUS:              " + str(status))
            if status['in_reply_to_status_id_str'] == tweetId:
                statuses.append(status['text'])
        return statuses

    def getReplies(self, tweetId):
        author = self.getAuthor(tweetId)
        if (author == "Tweet ID Handle Not Found") or (author == "Something Went Wrong"):
            print(author)
            return author
        print(author)
        statuses = self.getStatuses(author, tweetId)
        return statuses
