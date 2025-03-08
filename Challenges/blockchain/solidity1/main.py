import os
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for session handling

# Correct answers
answers = {
	'q1': 'withdraw()',
	'q2': 'function withdraw() public onlyOwner',
	'q3': 'nej',
	'q4': 'owner'
}

def get_flag():
	"""Reads the flag from a file if available."""
	flag_path = "flag.txt"
	if os.path.exists(flag_path):
		with open(flag_path, "r") as file:
			return file.read().strip()

@app.route('/', methods=['GET', 'POST'])
def home():
	message = ""
	flag = None

	if 'progress' not in session:
		session['progress'] = {}

	if request.method == 'POST':
		question = request.form.get('question')
		answer = request.form.get('answer', "")

	print(answer)
	print(question)


	if question in answers and answer == answers[question]:
		session['progress'][question] = answer
		session.modified = True
	else:
		message = "Incorrect answer. Try again!"

	if all(q in session['progress'] for q in answers):
		flag = get_flag()

	return render_template('index.html', message=message, flag=flag, progress=session['progress'])

if __name__ == '__main__':
	app.run()