#You will need to PIP INSTALL tweepy for this to work and also create a twitter API. Run this on your own machine, not in this Repl. 
import tweepy
import time

consumer_key = 'H3Y22dDL2eBRfGvuWtMjLtUbI'
consumer_secret = 'TvEcBjMYNuTwch1J7ZeRL055umrfcrwGal2WbpyiZRKURnvtYd'
access_token = '1345275998-GvcBNGWJLbGWPfrFTDkHEk315WwlCmhfemkTuaO'
access_token_secret = 'MWh8V7AhLHlZZZO4lJV2499xA7PEHU165knhPuZOO4IP8'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name) #prints your name.
print (user.screen_name)
print (user.followers_count)

search = "python"
numberOfTweets = 2


def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(1000)

#Be nice to your followers. Follow everyone!
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
#   if follower.name == '':
    print(follower.name)
    follower.follow()


# # Be a narcisist and love your own tweets. or retweet anything with a keyword!
# for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
#     try:
#         tweet.favorite()
#         print('Retweeted the tweet')
#     except tweepy.TweepError as e:
#         print(e.reason)
#     except StopIteration:
#         break