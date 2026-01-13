# The GET method is used to request data from a server. 
# It appends data to the URL in a name-value pair format. 
# GET should not be used for sensitive data since URLs are visible in browser history.
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/square', methods=['GET'])
def squarenumber():
    num = request.args.get('num')
    
    if num is None:
        return render_template('squarenum.html')
    elif num.strip() == '':
        return "Please provide a number."
    try:
        square = float(num) ** 2
        return render_template('answer.html', squareofnum=square, number=num)
    except ValueError:
        return "Invalid input. Please enter a valid number."

if __name__ == '__main__':
    app.run(debug=True)