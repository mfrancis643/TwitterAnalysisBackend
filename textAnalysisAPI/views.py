from textAnalysisAPI.twitterAPI import TwitterApi
from textAnalysisAPI.textBlob import TextAnalysis
from textAnalysisAPI.Entities.TwitterResponseEntity import TwitterHttpResponse
from textAnalysisAPI.Entities.ErrorResponseEntity import ErrorHttpResponse
from django.http import HttpResponse

twitterInstance = TwitterApi()


def getTimeline(request, twitterHandle):
    twitterData = twitterInstance.getTimeline(twitterHandle)

    if isinstance(twitterData, str):
        return ErrorHttpResponse(twitterData).build()

    analysisInstance = TextAnalysis(getTweetMegaString(twitterData))
    score = analysisInstance.analyseTweet()

    twitterHttpResponse = TwitterHttpResponse(round(score, 2), twitterData)
    return twitterHttpResponse.build()


def getReplies(request, tweetId):
    twitterData = twitterInstance.getReplies(tweetId)

    if isinstance(twitterData, str):
        return ErrorHttpResponse(twitterData).build()

    analysisInstance = TextAnalysis(getTweetMegaString(twitterData))
    score = analysisInstance.analyseTweet()

    twitterHttpResponse = TwitterHttpResponse(round(score, 2), twitterData)
    return twitterHttpResponse.build()


def getHealth(request):
    return HttpResponse("ok")


def getTweetMegaString(twitterData):
    megaString = ""
    for tweet in twitterData:
        megaString += tweet + " "
    # score = TextAnalysis.analyseTweet(TextAnalysis, megaString)
    # score = ((score+1)/2)*10
    return megaString
