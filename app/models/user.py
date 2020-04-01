# -*- coding: utf-8 -*-
__author__ = 'Aaron'
__date__ = '2020/4/1 0001 21:11'

from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash

from app.models.base import Base, db


class User(Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), unique=True)
    _password = Column('password', String(100))
    email = Column(String(24), unique=True, nullable=False)
    auth = Column(SmallInteger, default=1)  # 1表示普通用户；2表示管理员

    @property
    def password(self):
        # password get fun
        return self._password

    @password.setter
    def password(self, raw):
        # password set fun
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname, secret, account):
        with db.auto_commit():
            # 静态方法，在对象中实例化对象本身
            user = User()
            user.nickname = nickname
            user.password = secret
            user.email = account
            db.session.add(user)
