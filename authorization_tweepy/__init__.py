import tweepy as tw
from tweepy import Status
import json

access_token = "98992106-OsffZtvTWPxeHCkA5G9golyjU4inlvb7XB6g0oDva"
access_token_secret = "eD0RE8AyfTDmyYnOKfWLo3XvjILKktRJOIoQnlmHCmbip"
consumer_key = "4jtRRPl3WvYyzPvRnNKRaaLGr"
consumer_secret = "dFr8l0HDQ2RA3sQhiTjkMvJs9ML38BLkEoofDNr50tBEOCmZNA"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.access_token = access_token
auth.access_token_secret = access_token_secret
api = tw.API(auth, wait_on_rate_limit=True)

statuses = []

q = 'previdencia social OR reforma da previdencia OR reforma da presidencia OR previdencia'

for tweet in tw.Cursor(api.search, q=q, lang="pt").items():
    print tweet._json['created_at']

# for tweet in tweets:
#     print tweet