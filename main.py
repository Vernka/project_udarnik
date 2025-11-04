from flask import Flask, request, render_template, redirect, url_for, session, flash
from flask_login import logout_user, LoginManager, login_user, current_user, login_required
import db_session
from werkzeug.security import generate_password_hash, check_password_hash
import os
import random
from Classes import User
from Classes import update_statistic
from Classes import get_statistic
import sqlite3

os.makedirs('db', exist_ok=True)
db_session.global_init('db/users.db')

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
    with open('static/Все слова.txt', 'r', encoding="utf-8") as f:
        all_words = [line.strip() for line in f]

    session['all_words_count'] = len(all_words)
    session['used_words'] = []  
    session['kolvo'] = 0
    session['yes'] = 0
    session.modified = True
    return redirect(url_for('exercise_words'))


@app.route("/exercise_words", methods=["GET", "POST"])
def exercise_words():
    if 'all_words_count' not in session:
        return redirect(url_for('words_file'))
    with open('static/Все слова.txt', 'r', encoding="utf-8") as f:
        all_words = [line.strip() for line in f]

    used_words = session.get('used_words', [])

    available_words = [word for word in all_words if word not in used_words]

    if request.method == 'POST' and 'action' in request.form and request.form['action'] == 'finish':
        return render_template('exercise_words.html', data=None,
                               yes=session.get('yes', 0), kolvo=session.get('kolvo', 0))

    if request.method == 'POST':
        button_type = request.form.get('button_type')
        current_word = request.form.get('current_word')

        if current_word and current_word not in used_words:
            used_words.append(current_word)
            session['used_words'] = used_words

        session['kolvo'] = session.get('kolvo', 0) + 1
        if button_type == 'yes':
            session['yes'] = session.get('yes', 0) + 1
        session.modified = True

        if current_user.is_authenticated:
            db_sess = db_session.create_session()
            update_statistic(db_sess, current_user, 'words', button_type == 'yes')
            db_sess.close()

    if available_words:
        word = random.choice(available_words)
        if '(' in word:
            meaning = word.split('(')[1].rstrip(')')
            word = word.split('(')[0]
        else:
            meaning = ""
    else:
        word = ""
        meaning = ""

    cogl = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ",
            "ъ", "ь"]
    glas = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]

    return render_template('exercise_words.html', data=word, meaning=meaning, cogl=cogl, glas=glas,
                           kolvo=session.get('kolvo', 0), yes=session.get('yes', 0))
@app.route("/such_file")
def such_file():
    with open('static/Существительные.txt', 'r', encoding="utf-8") as f:
        all_words = [line.strip() for line in f]

    session['all_such_count'] = len(all_words)
    session['used_such'] = []
    session['kolvo'] = 0
    session['yes'] = 0
    session.modified = True

    return redirect(url_for('exercise_such'))

@app.route("/exercise_such", methods=["GET", "POST"])
def exercise_such():
    if 'all_such_count' not in session:
        return redirect(url_for('such_file'))
    with open('static/Существительные.txt', 'r', encoding="utf-8") as f:
        all_such = [line.strip() for line in f]

    used_such = session.get('used_such', [])

    available_such = [word for word in all_such if word not in used_such]

    if request.method == 'POST' and 'action' in request.form and request.form['action'] == 'finish':
        return render_template('exercise_such.html', data=None,
                               yes=session.get('yes', 0), kolvo=session.get('kolvo', 0))

    if request.method == 'POST':
        button_type = request.form.get('button_type')
        current_word = request.form.get('current_word')

        if current_word and current_word not in used_such:
            used_such.append(current_word)
            session['used_such'] = used_such

        session['kolvo'] = session.get('kolvo', 0) + 1
        if button_type == 'yes':
            session['yes'] = session.get('yes', 0) + 1
        session.modified = True

        if current_user.is_authenticated:
            db_sess = db_session.create_session()
            update_statistic(db_sess, current_user, 'such', button_type == 'yes')
            db_sess.close()

    if available_such:
        word = random.choice(available_such)
        if '(' in word:
            meaning = word.split('(')[1].rstrip(')')
            word = word.split('(')[0]
        else:
            meaning = ""
    else:
        word = ""
        meaning = ""

    cogl = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ",
            "ъ", "ь"]
    glas = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]

    return render_template('exercise_such.html', data=word, meaning=meaning, cogl=cogl, glas=glas,
                           kolvo=session.get('kolvo', 0), yes=session.get('yes', 0))

@app.route("/pri_file")
def pri_file():
    with open('static/Прилагательные и причастия.txt', 'r', encoding="utf-8") as f:
        all_words = [line.strip() for line in f]

    session['all_pri_count'] = len(all_words)
    session['used_pri'] = []
    session['kolvo'] = 0
    session['yes'] = 0
    session.modified = True

    return redirect(url_for('exercise_pri'))


@app.route("/exercise_pri", methods=["GET", "POST"])
def exercise_pri():
    if 'all_pri_count' not in session:
        return redirect(url_for('pri_file'))
    with open('static/Прилагательные и причастия.txt', 'r', encoding="utf-8") as f:
        all_pri = [line.strip() for line in f]

    used_pri = session.get('used_pri', [])

    available_pri = [word for word in all_pri if word not in used_pri]

    if request.method == 'POST' and 'action' in request.form and request.form['action'] == 'finish':
        return render_template('exercise_pri.html', data=None,
                               yes=session.get('yes', 0), kolvo=session.get('kolvo', 0))

    if request.method == 'POST':
        button_type = request.form.get('button_type')
        current_word = request.form.get('current_word')

        if current_word and current_word not in used_pri:
            used_pri.append(current_word)
            session['used_pri'] = used_pri

        session['kolvo'] = session.get('kolvo', 0) + 1
        if button_type == 'yes':
            session['yes'] = session.get('yes', 0) + 1
        session.modified = True

        if current_user.is_authenticated:
            db_sess = db_session.create_session()
            update_statistic(db_sess, current_user, 'pri', button_type == 'yes')
            db_sess.close()

    if available_pri:
        word = random.choice(available_pri)
        if '(' in word:
            word = word.split('(')[0]
    else:
        word = ""

    cogl = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ",
            "ъ", "ь"]
    glas = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]

    return render_template('exercise_pri.html', data=word, cogl=cogl, glas=glas,
                           kolvo=session.get('kolvo', 0), yes=session.get('yes', 0))


@app.route("/glag_file")
def glag_file():
    with open('static/Глаголы.txt', 'r', encoding="utf-8") as f:
        all_words = [line.strip() for line in f]

    session['all_glag_count'] = len(all_words)
    session['used_glag'] = []
    session['kolvo'] = 0
    session['yes'] = 0
    session.modified = True

    return redirect(url_for('exercise_glag'))


@app.route("/exercise_glag", methods=["GET", "POST"])
def exercise_glag():
    if 'all_glag_count' not in session:
        return redirect(url_for('glag_file'))
    with open('static/Глаголы.txt', 'r', encoding="utf-8") as f:
        all_glag = [line.strip() for line in f]

    used_glag = session.get('used_glag', [])

    available_glag = [word for word in all_glag if word not in used_glag]

    if request.method == 'POST' and 'action' in request.form and request.form['action'] == 'finish':
        return render_template('exercise_glag.html', data=None,
                               yes=session.get('yes', 0), kolvo=session.get('kolvo', 0))

    if request.method == 'POST':
        button_type = request.form.get('button_type')
        current_word = request.form.get('current_word')

        if current_word and current_word not in used_glag:
            used_glag.append(current_word)
            session['used_glag'] = used_glag

        session['kolvo'] = session.get('kolvo', 0) + 1
        if button_type == 'yes':
            session['yes'] = session.get('yes', 0) + 1
        session.modified = True

        if current_user.is_authenticated:
            db_sess = db_session.create_session()
            update_statistic(db_sess, current_user, 'glag', button_type == 'yes')
            db_sess.close()

    if available_glag:
        word = random.choice(available_glag)
        if '(' in word:
            word = word.split('(')[0]
    else:
        word = ""

    cogl = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ",
            "ъ", "ь"]
    glas = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]

    return render_template('exercise_glag.html', data=word, cogl=cogl, glas=glas,
                           kolvo=session.get('kolvo', 0), yes=session.get('yes', 0))
@app.route("/dn_file")
def dn_file():
    with open('static/Деепричастия и наречия.txt', 'r', encoding="utf-8") as f:
        all_words = [line.strip() for line in f]

    session['all_dn_count'] = len(all_words)
    session['used_dn'] = []
    session['kolvo'] = 0
    session['yes'] = 0
    session.modified = True

    return redirect(url_for('exercise_dn'))


@app.route("/exercise_dn", methods=["GET", "POST"])
def exercise_dn():
    if 'all_dn_count' not in session:
        return redirect(url_for('dn_file'))
    with open('static/Деепричастия и наречия.txt', 'r', encoding="utf-8") as f:
        all_dn = [line.strip() for line in f]

    used_dn = session.get('used_dn', [])

    available_dn = [word for word in all_dn if word not in used_dn]

    if request.method == 'POST' and 'action' in request.form and request.form['action'] == 'finish':
        return render_template('exercise_dn.html', data=None,
                               yes=session.get('yes', 0), kolvo=session.get('kolvo', 0))

    if request.method == 'POST':
        button_type = request.form.get('button_type')
        current_word = request.form.get('current_word')

        if current_word and current_word not in used_dn:
            used_dn.append(current_word)
            session['used_dn'] = used_dn

        session['kolvo'] = session.get('kolvo', 0) + 1
        if button_type == 'yes':
            session['yes'] = session.get('yes', 0) + 1
        session.modified = True

        if current_user.is_authenticated:
            db_sess = db_session.create_session()
            update_statistic(db_sess, current_user, 'dn', button_type == 'yes')
            db_sess.close()

    if available_dn:
        word = random.choice(available_dn)
        if '(' in word:
            word = word.split('(')[0]
    else:
        word = ""

    cogl = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ",
            "ъ", "ь"]
    glas = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]

    return render_template('exercise_dn.html', data=word, cogl=cogl, glas=glas,
                           kolvo=session.get('kolvo', 0), yes=session.get('yes', 0))

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
@login_required
def statistic():
    try:
        stats = get_statistic(current_user)
        return render_template('statistic.html', stats=stats)
    except Exception as e:
        return f"Ошибка при загрузке статистики: {str(e)}"


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "GET":
        return render_template("sign_in.html")
    elif request.method == "POST":
        login = request.form.get('login', '').strip()
        password = request.form.get('password', '').strip()

        if not login or not password:
            flash('Эти поля обязательны для заполнения', 'error')
            return render_template("sign_in.html")

        session_db = db_session.create_session()
        try:
            user = session_db.query(User).filter(User.login == login).first()
            if user and check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash('Вход выполнен успешно', 'success')
                return redirect("/")
            else:
                flash('Неверный логин или пароль', 'error')
                return render_template("sign_in.html")
        except Exception as e:
            flash(f'Ошибка при входе: {str(e)}', 'error')
            return render_template("sign_in.html")
        finally:
            session_db.close()

@app.route('/sign_out')
def sign_out():
    logout_user()
    return redirect('/')


@app.route("/registration", methods=["GET", "POST"])
def reg_users():
    if request.method == "GET":
        return render_template("reg.html")
    elif request.method == "POST":
        login = request.form.get('login', '').strip()
        password = request.form.get('password', '').strip()

        if not login or not password:
            flash('Введите логин и пароль', 'error')
            return render_template("reg.html")

        if len(login) < 3:
            flash('Логин должен содержать не менее 3 символов', 'error')
            return render_template("reg.html")

        if len(password) < 4:
            flash('Пароль должен содержать не менее 4 символов', 'error')
            return render_template("reg.html")

        session_db = db_session.create_session()
        try:
            existing_user = session_db.query(User).filter(User.login == login).first()
            if existing_user:
                flash('Пользователь с таким логином уже существует', 'error')
                return render_template("reg.html")

            new_user = User(
                login=login,
                password=generate_password_hash(password)
            )

            session_db.add(new_user)
            session_db.commit()

            login_user(new_user, remember=True)
            flash('Регистрация прошла успешно!', 'success')
            return redirect("/")

        except Exception as e:
            session_db.rollback()
            flash(f'Ошибка при регистрации: {str(e)}', 'error')
            return render_template("reg.html")
        finally:
            session_db.close()

if __name__ == "__main__":
    app.run(port="5000", host="127.0.0.1", debug=True)

