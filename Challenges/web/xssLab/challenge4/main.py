from flask import Flask, request, render_template_string, redirect, url_for
import threading
import time

app = Flask(__name__)

# Store user messages
messages = []

# Store "stolen" flags
stolen_flags = []

# Fake admin flag
ADMIN_FLAG = "FLAG{this_is_a_fake_admin_flag}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form.get('message', '')
        messages.append(message)
        return redirect(url_for('index'))
    
    return render_template_string("""
    <h1>XSS Demo Lab</h1>
    <form method="POST">
        <input name="message" placeholder="Enter your message or XSS payload" style="width:400px;">
        <button type="submit">Submit</button>
    </form>
    <h2>Messages</h2>
    {% for msg in messages %}
        <div style="border:1px solid gray; padding:5px; margin:5px;">{{ msg | safe }}</div>
    {% endfor %}
    """, messages=messages)

@app.route('/steal')
def steal():
    stolen = request.args.get('cookie')
    if stolen:
        stolen_flags.append(stolen)
        print(f"[!] Cookie stolen: {stolen}")
    return '', 204

@app.route('/stolen')
def show_stolen():
    return "<br>".join(stolen_flags)

# Simulate an admin bot visiting the page with the flag
def admin_bot():
    with app.test_client() as client:
        while True:
            for message in messages:
                # Simulate visiting the page with a session cookie
                client.set_cookie('localhost', 'session', ADMIN_FLAG)
                client.get('/', headers={'User-Agent': 'AdminBot/1.0'})
            time.sleep(10)

# Start admin bot in background
threading.Thread(target=admin_bot, daemon=True).start()

if __name__ == '__main__':
    app.run(debug=True)