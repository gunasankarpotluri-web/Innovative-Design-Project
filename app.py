import os

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

@app.errorhandler(RequestEntityTooLarge)
def handle_file_too_large(error):
    return "File too large. Maximum file size is 10 MB.", 413

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    uploaded_file = request.files.get("image")

    if uploaded_file is None:
        return "No image uploaded", 400

    filename = secure_filename(uploaded_file.filename)

    if '.' not in filename:
        return "File has no extension", 400
    
    extension = filename.rsplit('.', 1)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        return "Unsupported file type", 400

    upload_folder = "uploads"
    file_path = os.path.join(upload_folder, filename)
    uploaded_file.save(file_path)
    print(file_path)
    return "Image received!"

if __name__ == '__main__':
    app.run(debug=True)