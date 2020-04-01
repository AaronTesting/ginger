# -*- coding: utf-8 -*-
__author__ = 'Aaron'
__date__ = '2020/4/1 0001 20:33'

from wtforms import ValidationError
from wtforms import Form
from wtforms import IntegerField
from wtforms import StringField
from wtforms.validators import DataRequired, Email, Regexp
from wtforms.validators import length

from app.libs.enums import ClientTypeEnum
from app.models.user import User


class ClientForm(Form):
    account = StringField(validators=[DataRequired(), length(min=6, max=16)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='invalidate email')
    ])
    secret = StringField(validators=[
        DataRequired(),
        # password can only include letters , numbers and "_"
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=2, max=22)])
    # 账号是否存在
    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()