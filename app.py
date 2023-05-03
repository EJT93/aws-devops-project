from flask import Flask
app = Flask(__name__)

#base route for the application
@app.route('/')
def hello_world():
    return 'Hello, simple Flask application'