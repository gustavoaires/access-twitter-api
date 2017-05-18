from twitterscraper import query_tweets
import json

query = "previdencia OR reforma da presidencia OR reforma da previdencia since:2017-05-01 until:2017-05-02"

tweets_list = []

outfile = open('tweets_01_05.json', 'w')

for tweet in query_tweets(query):
    new_tweet = {}
    user = tweet.user
    new_tweet['screen_name'] = user
    new_tweet['id'] = tweet.id
    new_tweet['text'] = tweet.text
    tweets_list.append(new_tweet)
    json.dump(new_tweet, outfile)
    outfile.write("\n")

outfile.close()