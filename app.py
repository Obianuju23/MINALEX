from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    return 'Hi,{}'. format(name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
