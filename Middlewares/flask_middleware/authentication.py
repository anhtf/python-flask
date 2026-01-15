from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = "ANHTDH"

@app.before_request
def check_authen():
    token = request.headers.get("Authorization")
    if token != f"Bearer {API_KEY}":
        return jsonify({"error": "Unauthorized"}), 401
    
    
@app.route('/protected')
def protected():
    return jsonify({"message": "Welcome to the protected route!"})

if __name__ == "__main__":
    app.run(debug=True)