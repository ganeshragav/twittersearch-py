#!/usr/bin/python
import json
import tweepy
import csv
import unicodecsv
# Place your respective keys here
consumer_key=""
consumer_secret=""
api_key=""
api_secret=""

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(api_key,api_secret)

class Listeners(tweepy.StreamListener):
	def on_data(self,data):
		c = unicodecsv.writer(open("tweets.csv", "a"))
		streamed=json.loads(data)
		c.writerow([streamed['user']['screen_name'], streamed['text'],streamed["created_at"],streamed["user"]["name"],streamed["source"]])
	#	rows=[streamed["created_at"],streamed["text"].encode('ascii','ignore'),streamed["source"],streamed["in_reply_to_screen_name"],streamed["user"]["name"],streamed["user"]["screen_name"],streamed["user"]["time_zone"],streamed["user"]["profile_image_url"],streamed["user"]["default_profile_image"],streamed["user"]["friends_count"],streamed["user"]["followers_count"]]
#		c.writerow(rows)
f = open('keywords.txt', 'r')
array=[]
tweets=tweepy.streaming.Stream(auth,Listeners())
for i in f:
	array.append(i.replace(" ","%20"))
tweets.filter(track=array,async=True)
