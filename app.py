from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """
    Método que retorna a string "Hello, world!"
    """
    return "Hello, world!"


@app.route("/about")
def about():
    """
    Método que retorna a string "Página Sobre"
    """
    return "Página Sobre"


if __name__ == "__main__":
    app.run(debug=True)
