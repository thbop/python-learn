from flask import Flask, render_template, request
from calc import *

app = Flask(__name__)

"""
Plaintext - straight text/code
Hyper Text - Fancy colors, fonts, scale (e.g. Word)
HTTP - Hyper Text Transfer Protocol
HTTPS - HTTP Secure
HTML - Hyper Text Markdown Language

HTTP Methods:
    GET - Gets HTML
    POST - Gets HTML, but also sends data (e.g. form data)
"""


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calc", methods=["GET", "POST"])
def calc():
    result = ""
    if request.method == "POST":
        user_input = request.form.get("user_input").strip()

        args = user_input.split()
        num1 = float(args[0])
        num2 = float(args[2])
        operator = args[1]
        result = execute_operation(num1, num2, operator)

    return render_template("calc.html", value=result)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

