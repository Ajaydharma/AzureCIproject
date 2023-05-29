from flask import Flask, jsonify

app = Flask(__name__)

# API 1: Hello World
@app.route('/hello')
def hello():
    return 'Hello, World!'

# API 2: Square a number
@app.route('/square/<int:num>')
def square(num):
    result = num * num
    return jsonify({'input': num, 'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
