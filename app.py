from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, Denis!</p>"


if __name__ == "__main__":
    app.run()
