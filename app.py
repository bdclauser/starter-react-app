from flask import FLASK

app = FLASK(__name__)


@app.route("/")
def index():
    return "This is the main page."


@app.route("/get-items")
def get_items():
    return "TODO: Implement Functionality"


if __name__ == "__main__":
    app.run()
