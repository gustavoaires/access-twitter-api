import urllib2
from bs4 import BeautifulSoup
import datetime as dt
import locale

locale.setlocale(locale.LC_ALL, 'turkish')

url = "http://twitter.com/search?q=akparti%20since%3A2015-05-01%20until%3A2015-06-05&amp;amp;amp;amp;amp;amp;lang=tr"
response = urllib2.urlopen(url)
html = response.read()
soup = BeautifulSoup(html)

tweets = soup.find_all('li', 'js-stream-item')

for tweet in tweets:
    if tweet.find('p', 'tweet-text'):
        text_user = tweet.find('span', 'username').text
        tweet_text = tweet.find('p', 'tweet-text').text.encode('utf-8')
        tweet_id = tweet.find['data-item-id']
        timestamp = tweet.find('a', 'tweet-timestamp')['title']
        tweet_timestamp = dt.datetime.strptime(timestamp, '%H:%M - %d %b %Y')