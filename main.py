import flask
from flask import render_template

app = flask.Flask(__name__)

def init_file():
    file = []
    with open("static/data.txt", "r", encoding="utf-8") as f:
        file = f.readlines()

    return render_template("theory.html", data=file)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/exercise")
def exercise():
    return render_template("exercise.html")

@app.route("/exercise_word")
def exercise_word():
    return render_template("exercise_word.html")

@app.route("/theory")
def theory():
    return render_template("theory.html")

@app.route("/out")
def out():
    return render_template("out.html")

@app.route("/reg")
def reg():
    return render_template("reg.html")


if __name__ == "__main__":
    app.run(port="5000", host="127.0.0.1")