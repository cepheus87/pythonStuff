from flask import Flask, escape, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Index"


@app.route('/hello')
def hello():
    return "Hello, World!"


@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


# ending "/" difference
@app.route('/projects/')   # like directory - URL without a trailing slash, Flask redirects you to the canonical URL with the trailing slash
def projects():
    return 'The project page'


@app.route('/about')  # like file - Accessing the URL with a trailing slash produces a 404 “Not Found” error.
def about():
    return 'The about page'


# handling urls
with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello'))
    print(url_for('hello', next='/'))
    print(url_for('profile', username='John Doe'))


if __name__ == "__main__":
    app.run(debug=True)


