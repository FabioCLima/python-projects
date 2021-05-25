from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'


@app.route('/api')
def api():
    return jsonify(data={'name': 'Fabio Carvalho Lima'})


if __name__ == "__main__":
    app.run(debug=True)
