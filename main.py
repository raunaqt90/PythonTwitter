from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
  #return 'Welcome to Raptor Twitter'
  return '''
  <form method="POST" action="postoffice">
    <lable>What is happening?</label>
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
  return 'Successfully received tweet: ' + tweet + ' Username: ' + username


app.run(host='0.0.0.0', port=81)
