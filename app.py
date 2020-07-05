from flask import Flask, request, jsonify, render_template
from service import ToDoService
from models import Schema

import json

app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/todo/<query>")
def hello_name(query):
    return ToDoService().listStuff()


@app.route("/todo/", methods=["GET"])
def list_todo():
    response = ToDoService().listStuff()
    return response


@app.route("/todo", methods=["POST"])
def create_todo():
    return jsonify(ToDoService().create(request.get_json()))


if __name__ == "__main__":
    Schema()
    app.run(debug=True)