# Features of Template Inheritance
# Code Reusability: Write common HTML structure once and reuse it across multiple pages.
# Better Maintainability: Updating the base template updates all inherited templates automatically.
# Separation of Concerns: Keeps the structure and content of web pages separate for better organization.
# Scalability: Easily add new pages without duplicating code

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)