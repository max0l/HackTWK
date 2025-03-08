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

if __name__ == '__main__':
	app.run()