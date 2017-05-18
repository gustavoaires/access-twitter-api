import authorization_twitter
import json

# searching for tweets

q = 'previdencia social'

count = 100
max_results = 1000

search_results = authorization_twitter.twitter_api.search.tweets(q=q, count=count, lang="pt")

statuses = search_results['statuses']

for _ in range(10): # 10*100 = 1000
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError, e: # No more results when next_results doesn't exist
        break
    # Create a dictionary from next_results, which has the following form:
    # ?max_id=313519052523986943&q=NCAA&include_entities=1
    kwargs = dict([ kv.split('=')
                    for kv in next_results[1:].split("&") ])
    search_results = authorization_twitter.twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']
    if len(statuses) > max_results:
        print len(statuses)
        break

print json.dumps(statuses[2], indent=1)

# listing statuses
# for status in statuses:
    # print "status text", json.dumps(status['text'], indent=2)

# for _ in range(len(statuses)):
#     # print "Length of the statuses: ", len(statuses)
#     try:
#         next_results = search_results['search_metadata']['next_results']
#     except KeyError, e: # no more results found
#         break
#     # creating a dictionary from next_results
#     kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])
#
#     search_results = authorization_twitter.twitter_api.search.tweets(**kwargs)
#     statuses += search_results['statuses']

# print len(statuses)

# printing one sample of the statuses
# print json.dumps(statuses[0], indent=2)

# extracting text, screen names and hashtags

# status_texts = [ status['text']
#     for status in statuses
# ]
#
# screen_names = [ user_mention['screen_name']
#     for status in statuses
#         for user_mention in status['entities']['user_mentions']
# ]
#
# hashtags = [ hashtag['text']
#     for status in statuses
#         for hashtag in status['entities']['hashtags']
# ]
#
# # compute a collection of all worlds from all tweets
# words = [ w
#     for t in status_texts
#         for w in t.split()
# ]
#
# ids = [ id
#     for status['id'] in statuses
# ]
#
# print "statuses", json.dumps(statuses[0]['id'], indent=1)
# print "status_texts", json.dumps(status_texts, indent=1)
# print "screen_names", json.dumps(screen_names, indent=1)
# print "hastags", json.dumps(hashtags, indent=1)
# print "words", json.dumps(words, indent=1)

# creating a basic frequency distribution from the words in tweets

# for item in [words, hashtags, screen_names, status_texts]:
#     c = Counter(item)
#     print c.most_common()[:10] # top 10
#     print

# using prettytable to display the results of most common words

# for label, data in (('Word', words),
#                     ('Screen Name', screen_names),
#                     ('Hashtag', hashtags)):
#     pt = PrettyTable(field_names=[label, 'Count'])
#     c = Counter(data)
#     [ pt.add_row(kv) for kv in c.most_common()[:10] ]
#     pt.align[label], pt.align['Count'] = 'l', 'r'
    # print pt

# calculating lexical diversity

# def lexical_diversity(tokens):
#     return 1.0*len(set(tokens))/len(tokens)

# a function to calculate the average number of words per tweet

# def average_words(statuses):
#     total_words = sum([ len(s.split()) for s in statuses])
#     return 1.0*total_words/len(statuses)

# print lexical_diversity(words)
# print lexical_diversity(hashtags)
# print lexical_diversity(screen_names)
# print average_words(status_texts)