import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'rtJirTWooR6EVA3QfUiiaw'
consumer_secret = 'DDRXKI4NEjxEinz9J3pHvlZTD1nRGXi3DtG6MEguYI'
access_token = '19890536-IgyCUACJdLHsgfPmKySe48Yc1nNjhKLdt5chdXrro'
access_secret = 'B8EhIvddVvtrIhKNHDVmfTS1aZHpu9LjL3Jj2cgDJJWvE'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)