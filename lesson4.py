# Accessing dynamic data using JSON
# API

from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
     {
          'id': 1,
          'title': 'Data Analyst',
          'location': 'Bengaluru, India',
          'salary': 'Rs. 10,00,000'
     },
     {
          'id': 2,
          'title': 'Data Scientist',
          'location': 'Remote',
          'salary': 'Rs. 12,00,000'
     },
     {
          'id': 3,
          'title': 'Frontend Engineer',
          'location': 'Tampa, USA',
     },
     {
          'id': 4,
          'title': 'Backend Engineer',
          'location': 'Remote',
          'salary': 'Rs. 15,00,000'
     }
]


@app.route('/')
@app.route('/home')
def home_page():
     return render_template('lesson3.html', jobs = JOBS, companyName = 'CASA')


@app.route("/jobs")
def list_jobs():
     return jsonify(JOBS)


if __name__ == "__main__":
     app.run(host = '0.0.0.0', debug = True)