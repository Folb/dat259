from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello World"

@app.route('/new')
def new():
    return "Post new values"

@app.route('/new/temperature')
def newTypeSpesific():
    d = request.from_json(force=True)
    return "d"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
