import flask
from flask import render_template, url_for, redirect
import random


app = flask.Flask(__name__)


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

@app.route("/exercise_such")
def exercise_such():
    cogl = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ",
            "ъ", "ь"]
    glas = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    such = []
    zn = {}
    with open('static/Существительные.txt', 'r', encoding="utf-8") as f:
        line = f.readline()
        while line:
            line = line.rstrip()
            if len(line.split("(")) != 1:
                odin = line[:5]
                such.append(odin)
                dop = line[7:-1]
                zn[odin] = dop
            else:
                such.append(line)
            line = f.readline()
    if such:
        word = random.choice(such)
    else:
        word = ""
    return render_template('exercise_such.html', data=word, cogl=cogl, glas=glas)



@app.route("/theory")
def theory():
    with open('static/Слова.txt', 'r', encoding="utf-8") as f:
        line = f.read()
    return render_template('theory.html', data=line)

@app.route("/statistic")
def statistic():
    return render_template("statistic.html")

@app.route("/sign_in")
def sign_in():
    return render_template("sign.html")

@app.route("/reg")
def reg():
    return render_template("reg.html")


if __name__ == "__main__":
    app.run(port="5000", host="127.0.0.1")
