# Create a new file named app.py and render HTML templates to build the front end.

# To insert data, first create a database table with Name, Email, City, Country, and Phone Number columns.
# Connect to the database using sqlite3.connect("database.db"). If the table doesn’t exist, create it.
# A button in index.html navigates to the participant list, retrieving data from the existing database.
# Use a Jinja template loop in HTML to dynamically display database entries.
# The participants function selects all columns from the table and retrieves data using fetchall

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/home')

def index():
    return render_template('index.html')

connect = sqlite3.connect('database.db')
connect.execute('CREATE TABLE IF NOT EXISTS PARTICIPANT(name TEXT, email TEXT, city TEXT, country TEXT, phone TEXT)')

@app.route('/join', methods = ['GET', 'POST'])
def join():
    if request.method == 'POST':
        name    = request.form['name']
        email   = request