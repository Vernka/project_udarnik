import flask
from flask import render_template, url_for, redirect, request
import random
import sqlite3


app = flask.Flask(__name__)

remain_words = []
remain_such = []
remain_pri = []
remain_glag = []
remain_dn = []
def table():
    conn = sqlite3.connect('users_db.sqlite')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login VARCHAR(20) NOT NULL,
            password VARCHAR(20) NOT NULL,
            statistic_word INT,
            statistic_such INT,
            statistic_pri INT,
            statistic_glag INT,
            statistic_dn INT,
        )
    ''')
    cursor.execute("PRAGMA table_info(films)")
    existing_columns = [column[1] for column in cursor.fetchall()]

    required_columns = ['genre', 'rating', 'description']
    for column in required_columns:
        if column not in existing_columns:
            if column == 'rating':
                cursor.execute(f"ALTER TABLE films ADD COLUMN {column} REAL")
            else:
                cursor.execute(f"ALTER TABLE films ADD COLUMN {column} TEXT")
            print(f"Добавлена конпка: {column}")

    conn.close()

def data_table():
    conn = sqlite3.connect('users_db.sqlite')
    cursor = conn.cursor()

    cursor.execute('''
            INSERT INTO Users (
                id,
                login,
                password,
                statistic_word,
                statistic_such,
                statistic_pri,
                statistic_glag,
                statistic_dn,
            )
        ''')
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
    with open('static/Все слова.txt', 'r', encoding="utf-8") as f:
        line = f.readline()
        while line:
            line = line.rstrip()
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
    global remain_dn
    cogl = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ",
            "ъ", "ь"]
    glas = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    dn = []
    with open('static/Деепричастия и наречия.txt', 'r', encoding="utf-8") as f:
        line = f.readline()
        while line:
            line = line.rstrip()
            dn.append(line)
            line = f.readline()
    remain_dn = dn.copy()
    if len(remain_dn) != 0:
        word = random.choice(remain_dn)
        remain_dn.remove(word)
    else:
        word = ""
    return render_template('exercise_dn.html', data=word, cogl=cogl, glas=glas)


@app.route("/exercise_dn", methods=["GET", "POST"])
def exercise_dn():
    a = []
    global remain_dn
    cogl = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ",
            "ъ", "ь"]
    glas = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    if remain_dn != a:
        word = random.choice(remain_dn)
        remain_dn.remove(word)
    else:
        word = ""
    return render_template('exercise_dn.html', data=word, cogl=cogl, glas=glas)

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