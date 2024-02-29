# Setting up a page using flask

# //To render webpage without ability to modify
# set FLASK_APP=[pythonfilename.py]
# flask run

# //To automatically reload changes
# set FLASK_DEBUG=1
# flask run

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
     return "<h1>Hello Arnav</h1>"


@app.route('/about/<username>')
def about_page(username):
     return f'<h1>This is the about page of {username}</h1>'