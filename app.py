from flask_cors import CORS
from flask import Flask, jsonify, request

app = Flask(__name__, instance_relative_config=True)
app.secret_key = ""
CORS(app)

@app.route('/hello', methods=['GET'])
def hello():    
    return 'Hello from the dummy app'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)

