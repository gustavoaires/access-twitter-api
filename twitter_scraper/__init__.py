from twitterscraper import query_tweets
import json

query = "'previdencia' OR 'reforma da presidencia' OR 'reforma da previdencia' since:2017-03-25 until:2017-03-26"

tweets_list = []

outfile = open('tweets_25_03.json', 'w')

for tweet in query_tweets(query):
    new_tweet = {}
    new_tweet['screen_name'] = tweet.user
    new_tweet['id'] = tweet.id
    new_tweet['text'] = tweet.text
    tweets_list.append(new_tweet)
    json.dump(new_tweet, outfile)
    outfile.write("\n")

outfile.close()