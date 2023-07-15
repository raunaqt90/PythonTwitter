import db

def get_all_tweets():
  return db.get_all_tweets()


def add_tweets(tweet, username):
 db.create_tweet(username, tweet)


def get_tweets_by_username(username):
  return db.get_tweets_by_username(username)
