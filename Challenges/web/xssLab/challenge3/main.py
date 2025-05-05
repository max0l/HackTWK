from flask import Flask
from flask import render_template, abort, url_for, session

'''Simple Backend Server for XSS Lab'''

app = Flask(__name__)

@app.route('/', methods=['GET'])
app.config['SECRET_KEY'] = 'CHANGEME'
def home():
	session['flag'] = ''
	return render_template('index.html')

@app.route('/thirdEncounter', methods=['GET'])
def thirdEncounter():
	return render_template('thirdEncounter.html')

if __name__ == '__main__':
	print('Welcome to XSS Lab...:)')
	app.run()