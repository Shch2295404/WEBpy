# This code creates a Flask web application with four routes:
# "/" and "//" are for the hello_world function, which checks if the provided password is "1519" and returns a message accordingly.
# "/index/" renders the "index.html" template.
# "/contacts/" renders the "contacts.html" template.
# "/blog/" renders the "blog.html" template.
# Lastly, it runs the Flask application if the script is executed directly.
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/<password>/")
def hello_world(password=None):
    if password == "1519":
        return f"Доступ разрешён"
    else:
        return f"Доступ запрещён"


@app.route("/index/")
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
