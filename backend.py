from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/double", methods=["POST"])
def double_number():
    data = request.get_json()
    number = data["number"]
    return jsonify(result=number * 2)

if __name__ == "__main__":
    app.run(debug=True)