tweets = []  #list


def get_all_tweets():
  return tweets


def add_tweets(tweet, username):
  # create a dictionary
  t = {'username': username, 'tweet': tweet}
  tweets.append(t)


def get_tweets_by_username(username):
  # create a new list for the matching tweets
  user_tweets = []
  # go through the entire list of tweets one by one
  for tweet in tweets:
    # if the username matches username parameter, include it in the new list
    if (tweet.get('username') == username):
      user_tweets.append(tweet)
  # return th new list of tweets
  return user_tweets
