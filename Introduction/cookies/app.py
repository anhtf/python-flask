from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods = ['POST', 'GET']) 
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('cookie.html'))
        resp.set_cookie('userID', user)
        return resp
    else:
        return render_template('setcookie.html')
    
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return f'Welcome back {name}'

if __name__ == '__main__':
    app.run(debug = True)
