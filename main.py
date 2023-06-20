from flask import Flask, request, redirect, url_for

app = Flask(__name__)
tweets = []

current_user = ''


def get_html_form(action, header, fieldtitle, fieldname, buttonvalue):
  return f'''
   <form method="POST" action={action}>
   <h3>{header}</h3>
      {fieldtitle}: <input type="text" name="{fieldname}"/>
      <input type="submit" value="{buttonvalue}">
    </form>
  '''


@app.route('/')
def index():
  if current_user:
    return redirect(url_for('tweet'))
  else:
    return get_html_form('/login', 'Please Login', 'Username', 'username',
                         'LogIn')


@app.route('/login', methods=['POST'])
def login():
  global current_user
  current_user = request.form['username']
  return redirect(url_for('tweet'))


@app.route('/tweet')
def tweet():
  return get_html_form('/save-tweet', 'What is happening?', 'Tweet', 'tweet',
                       'Tweet')


@app.route('/save-tweet', methods=['POST'])
def contact():
  tweet = request.form.get('tweet')
  tweets.append(tweet)
  return 'Successfully received tweet: ' + tweet


@app.route('/my-tweets')
def my_tweets():
  tweet_html = ""
  for t in tweets:
    tweet_html += f'<li>{t}</li>'

  return f'''
    <h1>All my tweets</h1>
    <ol>{tweet_html}</ol>
  '''


app.run(host='0.0.0.0', port=81)
