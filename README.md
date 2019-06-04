**TwitterAnalysisBackend**

Simple Django REST app which returns the results of TextBlob's Natural Language Processing (NPL) analysis from fetched Twitter data.
This project is live and hosted on an [AWS EC2 Server](http://ec2-52-209-255-27.eu-west-1.compute.amazonaws.com)

**USAGE**

Three public endpoints (*shown in "urls.py"*):
1. /getTimeline/(TwitterHandle)
2. /getReplies/(tweetID)
3. /health

**CONSTRAINTS**

Twitter API also does not support fetching replies, and so a work around was developed in this app - depending on the popularity of the twitter account in question, it may not be possible to find replies with the amount of noise associated with the account.
- Twitter API only allows for 50 results to be fetched on a sandbox account - this could be fixed by paying the fee for a premium Twitter
Dev account.
- Code for a looping search exists to fetch replies, using the date of the last fetched tweet as the paramater for a new search, however this quickly surpasses the Twitter Dev account limits, locking the account, and so it is not in this repo.

*Although this is an entirely public facing app, a simple React.js UI exists (here)[https://github.com/mfrancis643/TwitterAnalysisFrontend]*