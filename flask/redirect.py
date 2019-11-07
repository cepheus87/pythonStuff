from flask import Flask, abort, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/login")
def login():
    abort(401)  # 401 means access denied
    this_is_never_executed()


def this_is_never_executed():
    return "AAAAAAAA"

"""
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
"""


if __name__ == "__main__":
    app.run(debug=True, port=5000)