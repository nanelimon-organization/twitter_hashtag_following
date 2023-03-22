from snscrape.modules import twitter
import json
from decouple import config
from model import Tweets
from msticpy.data.data_obfus import hash_string, hash_account, hash_item


hashtags = [config('HASHTAG')]

max_result = 1


def scrape_hastag(hashtag):
    scraper = twitter.TwitterHashtagScraper(hashtag)
    return scraper


def get_live_tweet():
    for index, i in enumerate(scrape_hastag(hashtags).get_items()):
        try:
            if index < max_result:
                json_tweet = json.loads(i.json())
                result = {
                    'device': json_tweet['sourceLabel'],
                    'tweet_url': hash_string(json_tweet['url']),
                    #'user_url': json_tweet['user']['url'],
                    'user_location': json_tweet['user']['location'],
                    'username': hash_account(json_tweet['username']),
                    'content': json_tweet['content'],
                    'publish_date': json_tweet['date'],
                    'hashtags': json_tweet['hashtags']
                }
                print(hash_string(result['tweet_url']))
                print(hash_account(result['username']))

                return result
            else:
                break
        except Exception as e:
            print(e)


def main():
    tweets = Tweets()
    a, b = '', ''
    _iter = 0
    while True:
        if _iter != 0:
            if a != b:
                b = a
                tweet = get_live_tweet()
                tweets.save(tweet)
            a = get_live_tweet()
        else:
            a = get_live_tweet()
        _iter += 1


if __name__ == "__main__":
    main()
