# Connecting flask to a pseudo database and returning the data onto the html site

from flask import Flask, render_template


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
          'salary': 'Rs. 13,00,000'
     }
]


@app.route('/')
@app.route('/home')
def home_page():
     return render_template('lesson3.html', jobs = JOBS, companyName = 'CASA')

if __name__ == '__main__':
     app.run(host = '0.0.0.0', debug = True)