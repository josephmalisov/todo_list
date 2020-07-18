from flask import Flask, request, jsonify, render_template
from service import ToDoService

import json

app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/newList")
def newList():
    return ToDoService().newList()

@app.route("/<url>")
def myurl(url):
    if (ToDoService().url_checker(url)):
        return render_template("index.html")
    return "Not Valid"

@app.route("/todo/<url>")
def hello_name(url):
    return ToDoService().listStuff(url)

# @app.route("/todo/", methods=["GET"])
# def list_todo():
#     response = ToDoService().listStuff()
#     return response

@app.route("/todo/<url>", methods=["POST"])
def create_todo(url):
    return jsonify(ToDoService().create(request.get_json("hey")))

@app.route("/todo/del", methods=["POST"])
def delete_todo():
    # jsonify(ToDoService().create(request.get_json()))
    return jsonify(ToDoService().deleteItem(request.get_json("hey")))

@app.route("/todo/done", methods=["POST"])
def check_todo():
    # jsonify(ToDoService().create(request.get_json()))
    return jsonify(ToDoService().checkItem(request.get_json("hey")))

@app.route("/todo/edit", methods=["POST"])
def edit_todo():
    # jsonify(ToDoService().create(request.get_json()))
    return jsonify(ToDoService().updateItem(request.get_json("hey")))


if __name__ == "__main__":
    app.run(debug=True)