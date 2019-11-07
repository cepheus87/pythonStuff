from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)  # look for templates in the templates folder.

"""
Case 1: a module:
/application.py
/templates
    /hello.html
    
Case 2: a package:
/application
    /__init__.py
    /templates
        /hello.html
"""

# static file
# url_for("static", filename="main.css")


if __name__ == "__main__":
    app.run(debug=True)
