from flask import Flask
from flask import render_template, abort, url_for, request, redirect

'''Simple Backend Server for XSS Lab'''

app  = Flask(__name__)
flag = "Hacktwk{ac63e50dc2eb71032f4d7fbc4c64dc41}"

@app.route('/', methods=['GET'])
def home():
	return render_template('index.html')


@app.route('/firstEncounter', methods=['GET'])
def firstEncounter():
	return render_template('firstEncounter.html')

@app.route('/xssFlag', methods=['POST']):
	if request.method == 'POST':
		if request.json()['xss'] == True:
			session['xss'] = flag
			return redirect('/firstEncounter', xss=flag)

if __name__ == '__main__':
	print('Welcome to XSS Lab...:)')
	app.run(host='0.0.0.0', port=5000)

# this needs testing -> does the 