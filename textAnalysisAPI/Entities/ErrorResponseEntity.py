from django.http import HttpResponse
import json


class ErrorHttpResponse:
    errorMsg = ""

    def __init__(self, parError):
        self.errorMsg = parError

    def getErrorMsg(self):
        return self.errorMsg

    def build(self):
        data = {}
        data['errorMsg'] = self.getErrorMsg()
        jsonBody = json.dumps(data)

        response = HttpResponse(jsonBody)
        return response
