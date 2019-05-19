try:
    import json
except ImportError:
    import simplejson as json
# Import the tweepy library
import tweepy

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '1121793302301433856-3e1RU0YssM8lGNpcAalhySgb0p1l1D'
ACCESS_SECRET = 'QbtrTB3YtGHrNHFkeTyIgzYSfUgwHv3g1RaaG1cAD7ATZ'
CONSUMER_KEY = 'YqmcIxxuPlkejk8WePk8Xkabf'
CONSUMER_SECRET = '1ZPyymtJG1Q4U7ZQTQo6nsNHi4uPxhtPUPTJ5EXjiOXSNr37Nb'

# Setup tweepy to authenticate with Twitter credentials:
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)


class GetTwitter:
    def getTweet(self, message):

        tweets = tweepy.Cursor(api.search,
                               q=message,
                               lang="en").items(1)

        message = next(tweets).text
        return message
