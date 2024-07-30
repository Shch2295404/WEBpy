# This code snippet creates a Flask web application
# with routes for "/" (index), "/contacts/", and "/blog/".
# The hello_world function checks if a password is provided in the URL
# and returns a message based on its value.
# If the password is "1519",
# it allows access; otherwise, it denies access.
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/<password>/")
def hello_world(password=None):
    if password == "1519":
        return f"Доступ разрешён"
    else:
        return f"Доступ запрещён"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")


@app.route("/blog/")
def blog():
    return render_template("blog.html")


if __name__ == "__main__":
    app.run()
