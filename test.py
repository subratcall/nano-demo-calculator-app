from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    data=request.get_json()
    name=data["name"]
    return 'Hello World!'+name
