from flask import Flask

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    ret = {
        'Message': 'Hello World',
        'Status Code': 200
        }
    return jsonify(ret)

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    x = data['x']
    y = data['y']
    sum = x+y
    ret = {
            'Message': sum,
            'Status Code': 200
    }
    return jsonify(ret)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    x = data['x']
    y = data['y']
    diff = x+y
    ret = {
            'Message': diff,
            'Status Code': 200
    }
    return jsonify(ret)

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
