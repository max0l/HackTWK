from flask import Flask, session, request, send_from_directory
from pyppeteer import launch
from werkzeug.utils import secure_filename
from werkzeug.security import safe_join
import os
import subprocess
import time
import json

app = Flask(__name__)
app.secret_key = b"Adding some entropy: " + os.urandom(24)

app.config['UPLOAD_FOLDER'] = '/app/uploads'

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filename = secure_filename(file.filename)
        file.save(safe_join(app.config['UPLOAD_FOLDER'], filename))
        extraction_id = os.urandom(24).hex()
        extraction_dir = safe_join(app.config['UPLOAD_FOLDER'], extraction_id)
        subprocess.call(['unzip', '-o', safe_join(app.config['UPLOAD_FOLDER'], filename), '-d', extraction_dir])
        command = ['unzip', '-l', safe_join(app.config['UPLOAD_FOLDER'], filename)]
        result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
        data = result.stdout
        lines = data.split('\n')
        file_lines = lines[3:-3] 
        files = []
        for line in file_lines:
            components = line.split()
            file_dict = {
                'length': int(components[0]),
                'date': components[1],
                'time': components[2],
                'name': components[3],
            }
            files.append(file_dict)
        total_line = lines[-2]  
        total_components = total_line.split()
        total_dict = {
            'total_length': total_components[0],
            'total_files': total_components[2] 
        }
        final_dict = {
            'archive': filename,
            'files': files,
            'total': total_dict
        }
        with open(safe_join(extraction_dir, 'index.json'), 'w') as f:
            json.dump(final_dict, f)
        os.remove(safe_join(app.config['UPLOAD_FOLDER'], filename))
        session['extraction_ids'] = session.get('extraction_ids', []) + [extraction_id]
        return extraction_id, 200

@app.route('/api/files', methods=['GET'])
def list_extractions():
    return {'extractions': session.get('extraction_ids', [])}, 200

@app.route('/api/files/<extraction_id>', methods=['GET'])
def list_files(extraction_id):
    if not all([e in "0123456789abcdef" for e in extraction_id]):
        return "Invalid extraction id", 400
    with open(safe_join(app.config['UPLOAD_FOLDER'], extraction_id, 'index.json'), 'r') as f:
        files = json.load(f)['files']
    return {'files': files}, 200

@app.route('/api/download/<extraction_id>/<filename>', methods=['GET'])
def download_file(extraction_id, filename):
    extraction_dir = safe_join(app.config['UPLOAD_FOLDER'], extraction_id)
    with open(safe_join(extraction_dir, 'index.json'), 'r') as f:
        files = json.load(f)['files']
    for file in files:
        if file['name'] == filename:
            filesize = file['length']
            break
    return send_from_directory(extraction_dir, filename, as_attachment=True, download_name=filename).make_conditional(request, filename, filesize), 200
    
@app.route('/api/flag')
def flag():
    if "admin" in session and session["admin"] == True:
        return subprocess.check_output(["/app/flag"]), 200
    return "You are not admin!", 403

@app.route('/api/admin/<extraction_id>')
async def admin(extraction_id:str):
    if not all([e in "0123456789abcdef" for e in extraction_id]):
        return "Invalid extraction id", 400
    url = "http://localhost:1337/#{}".format(extraction_id)
    browser = await launch(headless=True, executablePath='/usr/bin/chromium', args=['--no-sandbox'], handleSIGINT=False, handleSIGTERM=False, handleSIGHUP=False)
    page = await browser.newPage()
    await page.goto(url)
    await page.setCookie({"url": "http://localhost:1337", "name": "secret", "value": app.secret_key.hex()})
    time.sleep(3)
    await browser.close()
    return "Admin has looked at your files!", 200

@app.route('/')
def index():
    return send_from_directory('/app/static', 'index.html', mimetype="text/html"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
