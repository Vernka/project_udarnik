import flask
from flask import render_template, url_for, redirect, request, session
import random
import sqlite3


app = flask.Flask(__name__)
app.secret_key = 'my_secret_key_123'

remain_words = []
remain_such = []
remain_pri = []
remain_glag = []
remain_dn = []

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/exercise")
def exercise():
    return render_template("exercise.html")

@app.route("/exercise_word")
def exercise_word():
    return render_template("exercise_words.html")

@app.route("/words_file")
def words_file():
    global remain_words
    cogl = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ",
            "ъ", "ь"]
    glas = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    words = []
    zn = {}
    with open('static/Все слова.txt', 'r', encoding="utf-8") as f:
        line = f.readline()
        while line:
            line = line.rstrip()
            if len(line.split("(")) != 1:
                odin = line[:5]
                words.append(odin)
                dop = line[7:-1]
                zn[odin] = dop
            else:
                words.append(line)
            line = f.readline()
    remain_words = words.copy()
    if len(remain_words) != 0:
        word = random.choice(remain_words)
        remain_words.remove(word)
    else:
        word = ""
    return render_template('exercise_words.html', data=word, cogl=cogl, glas=glas)


@app.route("/exercise_words", methods=["GET", "POST"])
def exercise_words():
    a = []
    global remain_words
    cogl = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ",
            "ъ", "ь"]
    glas = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    if remain_words != a:
        word = random.choice(remain_words)
        remain_words.remove(word)
    else:
        word = ""
    return render_template('exercise_words.html', data=word, cogl=cogl, glas=glas)
@app.route("/such_file")
def such_file():
    global remain_such
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
    remain_such = such.copy()
    if len(remain_such) != 0:
        word = random.choice(remain_such)
        remain_such.remove(word)
    else:
        word = ""
    return render_template('exercise_such.html', data=word, cogl=cogl, glas=glas)


@app.route("/exercise_such", methods=["GET", "POST"])
def exercise_such():
    a = []
    global remain_such
    cogl = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ",
            "ъ", "ь"]
    glas = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    if remain_such != a:
        word = random.choice(remain_such)
        remain_such.remove(word)
    else:
        word = ""
    return render_template('exercise_such.html', data=word, cogl=cogl, glas=glas)

@app.route("/pri_file")
def pri_file():
    global remain_pri
    cogl = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ",
            "ъ", "ь"]
    glas = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    pri = []
    with open('static/Прилагательные и причастия.txt', 'r', encoding="utf-8") as f:
        line = f.readline()
        while line:
            line = line.rstrip()
            pri.append(line)
            line = f.readline()
    remain_pri = pri.copy()
    if len(remain_pri) != 0:
        word = random.choice(remain_pri)
        remain_pri.remove(word)
    else:
        word = ""
    return render_template('exercise_pri.html', data=word, cogl=cogl, glas=glas)


@app.route("/exercise_pri", methods=["GET", "POST"])
def exercise_pri():
    a = []
    global remain_pri
    cogl = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ",
            "ъ", "ь"]
    glas = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    if remain_pri != a:
        word = random.choice(remain_pri)
        remain_pri.remove(word)
    else:
        word = ""
    return render_template('exercise_pri.html', data=word, cogl=cogl, glas=glas)

@app.route("/glag_file")
def glag_file():
    global remain_glag
    cogl = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ",
            "ъ", "ь"]
    glas = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    glag = []
    with open('static/Глаголы.txt', 'r', encoding="utf-8") as f:
        line = f.readline()
        while line:
            line = line.rstrip()
            glag.append(line)
            line = f.readline()
    remain_glag = glag.copy()
    if len(remain_glag) != 0:
        word = random.choice(remain_glag)
        remain_glag.remove(word)
    else:
        word = ""
    return render_template('exercise_glag.html', data=word, cogl=cogl, glas=glas)


@app.route("/exercise_glag", methods=["GET", "POST"])
def exercise_glag():
    a = []
    global remain_glag
    cogl = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ",
            "ъ", "ь"]
    glas = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    if remain_glag != a:
        word = random.choice(remain_glag)
        remain_glag.remove(word)
    else:
        word = ""
    return render_template('exercise_glag.html', data=word, cogl=cogl, glas=glas)

@app.route("/dn_file")
def dn_file():
    cogl = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ",
            "ъ", "ь"]
    glas = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    dn = []
    session['kolvo'] = 0
    session['yes'] = 0
    with open('static/Деепричастия и наречия.txt', 'r', encoding="utf-8") as f:
        line = f.readline()
        while line:
            line = line.rstrip()
            dn.append(line)
            line = f.readline()
    session['remain_dn'] = dn.copy()
    if session['remain_dn']:
        word = random.choice(session['remain_dn'])
    else:
        word = ""
    return render_template('exercise_dn.html', data=word, cogl=cogl, glas=glas)


@app.route("/exercise_dn", methods=["GET", "POST"])
def exercise_dn():
    a = []
    cogl = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ",
            "ъ", "ь"]
    glas = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    if request.method == "POST":
        button_type = request.form.get('button_type')
        current_word = request.form.get('current_word')
        if current_word and 'remain_dn' in session and current_word in session['remain_dn']:
            session['remain_dn'].remove(current_word)
        if button_type == 'yes':
            session['kolvo'] = session.get('kolvo', 0) + 1
            session['yes'] = session.get('yes', 0) + 1
        elif button_type == 'no':
            session['kolvo'] = session.get('kolvo', 0) + 1
        session.modified = True

    if 'remain_dn' in session and session['remain_dn']:
        word = random.choice(session['remain_dn'])
    else:
        word = ""
    return render_template('exercise_dn.html', data=word, cogl=cogl, glas=glas, kolvo=session.get('kolvo', 0), yes=session.get('yes', 0))


@app.route("/theory")
def theory():
    sections = {}
    current_section = None
    with open('static/Слова.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if line.startswith('# '):
                current_section = line[2:].strip()
                sections[current_section] = []
            elif current_section:
                sections[current_section].append(line)

    return render_template('theory.html', sections=sections)


@app.route("/statistic")
def statistic():
    return render_template("statistic.html")

@app.route("/sign_in")
def sign_in():
    return render_template("sign.html")

@app.route("/reg", methods=["GET"])
def reg():
    return render_template("reg.html")

@app.route("/register_users", methods=["POST"])
def register_users():
    login = request.form['login']
    password = request.form['password']
    conn = sqlite3.connect('users_db.sqlite')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (login, password) VALUES (?, ?)", (login, password))
    conn.commit()
    conn.close()

    return "Пользователь успешно зарегистрирован!"


if __name__ == "__main__":

    app.run(port="5000", host="127.0.0.1")
