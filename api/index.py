from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/merge_pdfs', methods=['POST'])
def merge_pdfs():
    data = request.get_json()
    return data
