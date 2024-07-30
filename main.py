from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/<password>/")
def hello_world(password=None):
    if password == "1519":
        return f"Доступ разрешён"
    else:
        return f"Доступ запрещён"


@app.route("/")
def films():
    return render_template("index.html")


@app.route("/contacts/")
def person():
    return render_template("contacts.html")


@app.route("/blog/")
def about():
    return render_template("blog.html")


if __name__ == "__main__":
    app.run()
