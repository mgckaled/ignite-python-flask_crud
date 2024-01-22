from flask import Flask, request

from models.task import Task

app = Flask(__name__)

@app.route("/")
def init_server():
    return "Server is running"


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    print(data)
    return "test"


if __name__ == "__main__":
    app.run(debug=True)
