import flask
from flask import Flask, request, render_template, redirect, url_for, session, flash
from flask_login import logout_user, LoginManager, login_user, current_user
import db_session
from Classes import User
from werkzeug.security import generate_password_hash, check_password_hash
import os
import random
import sqlite3
os.makedirs('db', exist_ok=True)
db_session.global_init(True, 'db/users.db')

app = Flask(__name__)
app.secret_key = 'sanich_pomogi517'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'sign_in'

@login_manager.user_loader
def load_user(user_id):
    session_db = db_session.create_session()
    user = session_db.get(User, user_id)
    session_db.close()
    return user
app = flask.Flask(__name__)
app.secret_key = 'Sanich_pomogi517'

remain_words = []
remain_such = []
remain_pri = []
remain_glag = []
remain_dn = []
great = 0
all = 0

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
    if request.method == 'POST' and 'action' in request.form and request.form['action'] == 'finish':
        return render_template('exercise_dn.html', data=None, yes=session.get('yes', 0), kolvo=session.get('kolvo', 0), cogl=cogl, glas=glas)
    if request.method == 'POST':
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
    global great
    global all
    return render_template("statistic.html", great=great, all=all)

@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "GET":
        return render_template("sign_in.html")
    elif request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        if not login or not password:
            flash('Эти поля обязательны для заполнения', 'error')
            return redirect('/sign_in')
        session_db = db_session.create_session()
        try:
            user = session_db.query(User).filter(User.login == login).first()
            if user and check_password_hash(user.password, password):
                login_user(user)
                flash('Вход выполнен успешно', 'success')
                return redirect("/")
            else:
                flash('Неверный логин или пароль', 'error')
                return redirect('/sign_in')
        except Exception as e:
            flash(f'Ошибка при входе: {str(e)}', 'error')
            return redirect('/sign_in')
        finally:
            session_db.close()

@app.route('/sign_out')
def sign_out():
    logout_user()
    flash('Вы вышли из системы', 'info')
    return redirect('/')

@app.route("/registration", methods=["GET", "POST"])
def reg_users():
    if request.method == "GET":
        return render_template("reg.html")
    elif request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        if not login or not password:
            flash('Введите логин и пароль', 'error')
            return redirect('/registration')
        session_db = db_session.create_session()
        try:
            existing_user = session_db.query(User).filter(User.login == login).first()
            if existing_user:
                session_db.close()
                flash('Пользователь с таким логином уже существует', 'error')
                return redirect('/registration')

            new_user = User(
                login=login,
                password=generate_password_hash(password)
            )

            session_db.add(new_user)
            session_db.commit()

            login_user(new_user)
            flash('Регистрация прошла успешно!', 'success')
            return redirect("/")

        except Exception as e:
            session_db.rollback()
            flash(f'Ошибка при регистрации: {str(e)}', 'error')
            return redirect('/registration')
        finally:
            session_db.close()

if __name__ == "__main__":

    app.run(port="5000", host="127.0.0.1")

