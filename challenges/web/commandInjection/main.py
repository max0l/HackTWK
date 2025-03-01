import os,re 
from flask import Flask
from flask import render_template, abort, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	return render_template('index.html')

@app.route('/firstEncounter', methods=['GET'])
def firstEncounter():
	if request.method == 'GET':
			if request.args.get('param') != None:
				oupsi = request.args.get('param')
				baddie = (os.popen(f'ping -c 1 {oupsi}').read()).strip()
				return render_template('firstEncounter.html', args=baddie)
	return render_template('firstEncounter.html', args="Beautiful Content")

# sanitization -> commands
@app.route('/secondEncounter', methods=['GET'])
def secondEncounter():
	if request.method == 'GET':
			if request.args.get('param') != None:
				oupsi = request.args.get('param')
				if any(i in oupsi for i in ['whoami', 'cat', 'ls']):
					return render_template('secondEncounter.html', args="Please don't hack this site")
				baddie = (os.popen(f'ping -c 1 {oupsi}').read())
				return render_template('secondEncounter.html', args=baddie)
	return render_template('secondEncounter.html', args="Beautiful Content")


if __name__ == '__main__':
	app.run()