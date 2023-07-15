import sqlite3

conn = sqlite3.connect('tweets.db', check_same_thread=False)
cursor = conn.cursor()


def init():
  try:
    cursor.execute(
      'CREATE TABLE IF NOT EXISTS tweets (_id integer primary key autoincrement, tweet text, username text) '
    )
    cursor.execute(
      'CREATE TABLE IF NOT EXISTS users (_id integer primary key autoincrement, username text UNIQUE, password text) '
    )
  except sqlite3.OperationalError as e:
    print(e)
conn.commit()


def create_tweet(username, tweet):
  cursor.execute('INSERT INTO tweets VALUES (null, :t, :u)', {
    't': tweet,
    'u': username
  })


def create_user(username, password):
  cursor.execute('INSERT INTO users VALUES (null, :u, :p)', {
    'u': username,
    'p': password
  })


def get_all_tweets():
  cursor.execute('SELECT * FROM tweets')
  tweets = cursor.fetchall()
  return tweets


def get_tweets_by_username(username):
  cursor.execute('SELECT * FROM tweets WHERE username = :username',
                 {'username': username})
  tweets = cursor.fetchmany(10)
  return tweets


def get_user_by_username(username):
  cursor.execute('SELECT * FROM users WHERE username = :username',
                 {'username': username})
  user = cursor.fetchone()
  return user