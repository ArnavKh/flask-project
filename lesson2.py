# Linking flask to html file

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
     return render_template('lesson2.html')
