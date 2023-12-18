from flask import Flask
from flask import render_template, abort, url_for

'''Simple Backend Server for XSS Lab'''

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	return render_template('index.html')

@app.route('/firstEncounter', methods=['GET'])
def firstEncounter():
	return render_template('firstEncounter.html')

@app.route('/secondEncounter', methods=['GET'])
def secondEncounter():
	return render_template('secondEncounter.html')

@app.route('/thirdEncounter', methods=['GET'])
def thirdEncounter():
	return render_template('thirdEncounter.html')

@app.route('/fourthEncounter', methods=['GET'])
def fourthEncounter():
	return render_template('fourthEncounter.html')


if __name__ == '__main__':
	print('Welcome to XSS Lab...:)')
	app.run()