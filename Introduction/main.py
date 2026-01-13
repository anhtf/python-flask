from flask import Flask, redirect, url_for

app = Flask(__name__) # Flask(__name__): Creates the Flask app.

#@app.route('/') #Defines the home route (/).

#creates a function that is bound with '/' route and returns "HELLO" when the root page is accessed
def hello():
    return "Hello, World!"

#Variables in Flask are used to build a URL dynamically by adding the variable parts to the rule parameter. 
# #It is passed as keyword arguments to the route() decorator.
# Variable Rules
# A variable rule is defined using <variable-name> within the route.
# The captured variable is automatically passed as a keyword argument to the associated function.
# This feature helps build more flexible and interactive web applications by allowing dynamic content retrieval based on user input.
# Dynamic URLs Variable In Flask
# The following converters are available in Flask-Variable Rules:

# String - It accepts any text without a slash(the default).
# int - accepts only integers. ex =23 
# float - like int but for floating point values ex. = 23.9
# path - like the default but also accepts slashes.
# any - matches one of the items provided.
# UUID = accepts UUID strings.
@app.route('/hello/<name>')
def hello_t(name):
    return f"Hello, {name}!"

@app.route('/square/<int:num>')
def square(num):
    return f"The square of {num} is {num * num}"

# Using add_url_rule() to bind URL to function
@app.route('/admin')
def hello_admin():
    return "Hello, Admin!"
#http://localhost:5000/admin

@app.route('/guest/<guest>')
def hello_guest(guest):
    return f"Hello, {guest}!"
#http://localhost:5000/guest/anyname

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect (url_for('hello_guest', guest=name))
#http://localhost:5000/user/anyname


app.add_url_rule('/', 'hello', hello) 
# Tương đương với @app.route('/') provide routing technique so that user can remember the URLs. It is useful to access the web page directly without navigating from the Home page. It is done through the following route() decorator, to bind the URL to a function
# http://localhost:5000/hello
if __name__ == '__main__':
    app.run(debug=True)