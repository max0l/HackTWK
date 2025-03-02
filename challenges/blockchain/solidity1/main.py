import os,re 
from flask import Flask
from flask import render_template, abort, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	answers = [
		'withdraw()',
		'function withdraw() public onlyOwner',
		'nej',
		'owner'
    ]
    if request.method == 'POST':
        args = request.args.post()
        print('hello')

    return render_template('index.html')


if __name__ == '__main__':
	app.run()