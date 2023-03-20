from snscrape.modules import twitter
import json
from decouple import config


hashtag = [config('HASHTAG')]

max_result = 1


def scrape_hastag(hashtag):
    scraper = twitter.TwitterHashtagScraper(hashtag)
    return scraper


def get_live_tweet():
    for index, i in enumerate(scrape_hastag(hashtag).get_items()):
        if index < max_result:
            json_tweet = json.loads(i.json())
            result = {
                'device': json_tweet['sourceLabel'],
                'tweet_url': json_tweet['url'],
                'user_url': json_tweet['user']['url'],
                'user_location': json_tweet['user']['location'],
                'username': json_tweet['username'],
                'content': json_tweet['content'],
                'date': json_tweet['date'],
                'hashtags': json_tweet['hashtags']
            }
            return result
        else:
            break


def main():
    a, b = '', ''
    _iter = 0
    while True:
        if _iter != 0:
            if a != b:
                b = a
                print(get_live_tweet())
            a = get_live_tweet()
        else:
            a = get_live_tweet()
        _iter += 1


if __name__ == "__main__":
    main()
