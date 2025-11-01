from sqlalchemy import Column, Integer, String
from db_session import SqlAlchemyBase
from flask_login import UserMixin

class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(100), nullable=False)
    password = Column(String(200), nullable=False)
    all = Column(Integer, nullable=True, default=0)
    great = Column(Integer, nullable=True, default=0)
    all_words = Column(Integer, nullable=True, default=0)
    all_yes = Column(Integer, nullable=True, default=0)
    such_all = Column(Integer, nullable=True, default=0)
    such_yes = Column(Integer, nullable=True, default=0)
    pri_all = Column(Integer, nullable=True, default=0)
    pri_yes = Column(Integer, nullable=True, default=0)
    glag_all = Column(Integer, nullable=True, default=0)
    glag_yes = Column(Integer, nullable=True, default=0)
    dn_all = Column(Integer, nullable=True, default=0)
    dn_yes = Column(Integer, nullable=True, default=0)
    adedusers = Column(String(10), nullable=True, default='False')