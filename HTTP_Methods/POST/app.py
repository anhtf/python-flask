# The POST method is used to send data to the server for processing. 
# Unlike GET, it does not append data to the URL.
# Instead, it sends data in the request body, making it a better choice for sensitive or large data
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/square', methods=['GET', 'POST'])
def squarenumber():
    if request.method == 'POST':
        num = request.form.get('num')
        if num.strip() == '':   # Empty input
            return "<h1>Invalid number</h1>"
        square = int(num) ** 2
        return render_template('answer.html', squareofnum=square, num=num)
    return render_template('squarenum.html')

if __name__ == '__main__':
    app.run(debug=True, port = 2506)