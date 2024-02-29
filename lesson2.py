# Linking flask to html file

# The html file must be saved under folder names 'templates'

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
     return render_template('lesson2.html')