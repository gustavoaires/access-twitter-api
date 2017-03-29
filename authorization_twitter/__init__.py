import twitter
import json

# connecting to twitter

CONSUMER_KEY = '4jtRRPl3WvYyzPvRnNKRaaLGr'
CONSUMER_SECRET = 'dFr8l0HDQ2RA3sQhiTjkMvJs9ML38BLkEoofDNr50tBEOCmZNA'
OAUTH_TOKEN = '98992106-OsffZtvTWPxeHCkA5G9golyjU4inlvb7XB6g0oDva'
OAUTH_TOKEN_SECRET = 'eD0RE8AyfTDmyYnOKfWLo3XvjILKktRJOIoQnlmHCmbip'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# print twitter_api

# retrieving trends from worldwide and us

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

# print world_trends
# print
# print us_trends

# printing the result more nicely

# print
# print json.dumps(world_trends, indent=1)
# print
# print json.dumps(us_trends, indent=1)

# computing the intersection of two set of trends

world_trends_set = set([trend['name']
                   for trend in world_trends[0]['trends']])

us_trends_set = set([trend['name']
                     for trend in us_trends[0]['trends']])

common_trends = world_trends_set.intersection(us_trends_set)

# print common_trends