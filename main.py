from flask import Flask, request, redirect, url_for, render_template
from tweets import add_tweets, get_all_tweets, get_tweets_by_username

app = Flask(__name__)

current_user = ''


def get_html_form(action, header, fieldtitle, fieldname, buttonvalue):
  #MVC - Controller is passing values to View
  return render_template('form.html',
                         action=action,
                         header=header,
                         fieldtitle=fieldtitle,
                         fieldname=fieldname,
                         buttonvalue=buttonvalue)


@app.route('/')
def index():
  if current_user:
    return redirect(url_for('tweet'))
  else:
    return render_template('form.html',
                           action='/login',
                           header='Please Login',
                           fieldtitle='Username',
                           fieldname='username',
                           buttonvalue='LogIn')


@app.route('/login', methods=['POST'])
def login():
  global current_user
  current_user = request.form['username']
  return redirect(url_for('tweet'))


@app.route('/logout')
def logout():
  global current_user
  current_user = ''
  return redirect(url_for('index'))


@app.route('/tweet')
def tweet():
  return render_template('form.html',
                         action='/save-tweet',
                         header='What is happening?',
                         fieldtitle='Tweet',
                         fieldname='tweet',
                         buttonvalue='Tweet')


@app.route('/save-tweet', methods=['POST'])
def contact():
  tweet = request.form.get('tweet')
  add_tweets(tweet, current_user)
  return 'Successfully received tweet: ' + tweet


@app.route('/tweets/<username>')
@app.route('/tweets')
def user_tweets(username=None):
  if username:
    tweets = get_tweets_by_username(username)
  else:
    tweets = get_all_tweets()
  return render_template('tweets.html',
                         tweets=tweets,
                         current_user=current_user,
                         username = username)

app.run(host='0.0.0.0', port=81)