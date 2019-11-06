from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Index"


@app.route("/login", methods=["GET", "POST"])  # by default is only GET
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


@app.route("/login/log_form")
def show_the_login_form():
    return "LOG FORM"


def do_the_login():
    pass


@app.route("/query_example")
def query_example():
    #/query_example?language=Python&framework=Flask
    language = request.args.get("language")  # like calling dict
    framework = request.args["framework"]  # must be like calling dict
    return "<h1> The language is : {} and frm {}</h1>".format(language, framework)


@app.route("/form_example", methods=["GET", "POST"])
def form_example():
    if request.method == 'POST':
        lang = request.form.get("language")
        return f"submitted {lang}"
    else:
        return ''' <form method="POST">
        Language <input type="text", name="language">
        <input type="submit">
        </form>
        '''


if __name__ == "__main__":
    app.run(debug=True, port=5001)
