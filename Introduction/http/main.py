# HTTP method are provided by Flask
# Python Web Framework Flask support various HTTP protocols for data retrieval from the specified URL, these can be defined as:-

# Method	   Description
# GET	       This is used to send the data in an without encryption of the form to the server.
# HEAD	   provides response body to the form
# POST	   Sends the form data to server. Data received by POST method is not cached by server.
# PUT	       Replaces current representation of target resource with URL.
# DELETE	   Deletes the target resource of a given URL

# A web application often requires a static file such as javascript or a CSS file to render the display of the web page in browser. 
# Usually, the web server is configured to set them, but during development, these files are served as static folder in your package or next to the module

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)