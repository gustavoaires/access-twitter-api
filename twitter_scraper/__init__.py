from twitterscraper import query_tweets
from twitterscraper import main
import json

query = "previdencia OR reforma da presidencia OR reforma da previdencia since:2017-03-15 until:2017-03-22"

encoder = json.JSONEncoder()

# add code to save in a file

for tweet in query_tweets(query):
    print main.JSONEncoder(encoder).encode(tweet)