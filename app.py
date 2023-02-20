from flask import Flask, render_template, jsonify
import openai
import os
import numpy as np


app = Flask (__name__)

STRAINS = [
  {
    'id':1,
    'title': 'White Widow',
    'type': 'Indica',
    'effects': 'sedative'
  },
  {
    'id':2,
    'title': 'Grand Daddy Purp (GDP)',
    'type': 'Indica',
    'effects': 'sedative'
  },
{
    'id':3,
    'title': 'OG',
    'type': 'Indica',
    'effects': 'sedative'
  },
{
    'id':4,
    'title': 'Gelato 41',
    'type': 'Indica',
    'effects': 'sedative'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         strains=STRAINS)

  @app.route("/api/strains")
  def list_strains():
    return jsonify(STRAINS)

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
         if request.method == 'POST':
            # Handle the form submission
            username = request.form['username']
            password = request.form['password']
            # Add the user to your database
            return redirect('/login')
            # Render the sign up page
            return render_template('signup.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            # Handle the login form submission
            username = request.form['username']
            password = request.form['password']
            # Check if the username and password are correct
            # If they are, log the user in and redirect to the homepage
            return redirect('/')
        # Render the login page
        return render_template('login.html')




if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
