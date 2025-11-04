from sqlalchemy import Column, Integer, String, DateTime
from db_session import SqlAlchemyBase
from flask_login import UserMixin
import datetime


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(100), nullable=False)
    password = Column(String(200), nullable=False)
    adedusers = Column(String(10), nullable=True, default='False')
    total_sessions = Column(Integer, default=0)
    total_correct = Column(Integer, default=0)
    total_answers = Column(Integer, default=0)
    words_correct = Column(Integer, default=0)
    words_total = Column(Integer, default=0)
    such_correct = Column(Integer, default=0)
    such_total = Column(Integer, default=0)
    pri_correct = Column(Integer, default=0)
    pri_total = Column(Integer, default=0)
    glag_correct = Column(Integer, default=0)
    glag_total = Column(Integer, default=0)
    dn_correct = Column(Integer, default=0)
    dn_total = Column(Integer, default=0)
    last_active = Column(DateTime, default=datetime.datetime.utcnow)


def update_statistic(db_session, user, exercise_type, is_correct):
    """Обновляет статистику пользователя в БД"""
    fresh_user = db_session.query(User).filter(User.id == user.id).first()
    if not fresh_user:
        return
    fresh_user.total_answers = (fresh_user.total_answers or 0) + 1
    if is_correct:
        fresh_user.total_correct = (fresh_user.total_correct or 0) + 1

    if exercise_type == 'words':
        fresh_user.words_total = (fresh_user.words_total or 0) + 1
        if is_correct:
            fresh_user.words_correct = (fresh_user.words_correct or 0) + 1

    elif exercise_type == 'such':
        fresh_user.such_total = (fresh_user.such_total or 0) + 1
        if is_correct:
            fresh_user.such_correct = (fresh_user.such_correct or 0) + 1

    elif exercise_type == 'pri':
        fresh_user.pri_total = (fresh_user.pri_total or 0) + 1
        if is_correct:
            fresh_user.pri_correct = (fresh_user.pri_correct or 0) + 1

    elif exercise_type == 'glag':
        fresh_user.glag_total = (fresh_user.glag_total or 0) + 1
        if is_correct:
            fresh_user.glag_correct = (fresh_user.glag_correct or 0) + 1

    elif exercise_type == 'dn':
        fresh_user.dn_total = (fresh_user.dn_total or 0) + 1
        if is_correct:
            fresh_user.dn_correct = (fresh_user.dn_correct or 0) + 1

    fresh_user.last_active = datetime.datetime.utcnow()
    db_session.commit()


def get_statistic(user):
    """Возвращает статистику пользователя из БД"""
    total_correct = user.total_correct or 0
    total_answers = user.total_answers or 0

    stats = {
        'general': {
            'total_sessions': user.total_sessions or 0,
            'total_correct': total_correct,
            'total_answers': total_answers,
            'success_rate': round((total_correct / total_answers * 100), 1) if total_answers > 0 else 0
        },
        'by_type': {}
    }

    exercises = [
        ('words', 'Все слова', user.words_correct or 0, user.words_total or 0),
        ('such', 'Существительные', user.such_correct or 0, user.such_total or 0),
        ('pri', 'Прилагательные и причастия', user.pri_correct or 0, user.pri_total or 0),
        ('glag', 'Глаголы', user.glag_correct or 0, user.glag_total or 0),
        ('dn', 'Деепричастия и наречия', user.dn_correct or 0, user.dn_total or 0)
    ]

    for ex_type, name, correct, total in exercises:
        if total > 0:
            success_rate = round((correct / total * 100), 1) if total > 0 else 0
            stats['by_type'][ex_type] = {
                'name': name,
                'correct': correct,
                'total': total,
                'success_rate': success_rate
            }
    return stats
