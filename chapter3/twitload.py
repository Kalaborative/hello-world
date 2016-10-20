import tweepy
from random import choice
consumer_key = "1Va9E6ca4zb43q9JWf8mfZafc"
consumer_secret = "9tg89S9VcKf9AzfZh9CeMrsT8TjnbJN43RyTOxUX6uuddduE4W"

access_token = "114579331-oJa6oT6dKmciwyCcAGs0JjkY783ylyS3RJXPFocK"
access_secret = "vw7qWTONxEidKZnw3mVEKHD58uPF8NsyB19o2hCkX6jyN"

tweet_pos = []
tweet_neg = []
alreadySeen = []
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

tweet_list = api.home_timeline()
while True:
	if len(alreadySeen) == 20:
		break
	else:
		tweet1 = choice(tweet_list)
		if tweet1 not in alreadySeen:
			print tweet1.text.encode('utf-8')
			judge = input("1 pos, 2 neg, 3 skip: ")
			if judge == 1:
				tweet_pos.append(tweet1)
			elif judge == 2:
				tweet_neg.append(tweet1)
			alreadySeen.append(tweet1)
print "My positive tweets: "
for pos in tweet_pos:
	print pos.text.encode('utf-8')
print
print "My negative tweets: "
for neg in tweet_neg:
	print neg.text.encode('utf-8')
