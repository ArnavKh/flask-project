from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
     return render_template('lesson5-home.html')

app.route('/market')
def market_page():
     return render_template('lesson5-market.html')
