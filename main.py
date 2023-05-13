from flask import Flask, request

app = Flask(__name__)
tweets = []


@app.route('/')
def index():
  #return 'Welcome to Raptor Twitter'
  return '''
  <form method="POST" action="postoffice">
    <h3>What is happening?</h3>
    <br>
    Tweet <input type="text" name="tweet"/>
    <br>
    Username <input type="text" name="username"/>
    <br><br>
    <input type="submit" value="Tweet">
  </form>
  '''


@app.route('/postoffice', methods=['POST'])
def contact():
  tweet = request.form.get('tweet')
  username = request.form['username']
  tweets.append(tweet)
  return 'Successfully received tweet: ' + tweet + ' Username: ' + username


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
