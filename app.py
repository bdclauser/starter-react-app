from flask import FLASK, jsonify
import aws_controller

app = FLASK(__name__)


@app.route("/")
def index():
    return "This is the main page."


@app.route("/get-items")
def get_items():
    return jsonify(aws_controller.get_items())


if __name__ == "__main__":
    app.run()
