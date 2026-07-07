from flask import Flask, request, render_template
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


@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        ui = request.form.get("user_input").split(' ')
        output = execute_operation(float(ui[0]), float(ui[2]), ui[1])
    return render_template("index.html", output=output)



if __name__ == "__main__":
    app.run(debug=True)