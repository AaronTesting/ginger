# -*- coding: utf-8 -*-
__author__ = 'Aaron'
__date__ = '2020/4/1 0001 20:26'

from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint('client')
@api.route('/register', methods=['POST'])
def create_client():
    # 客户端使用 json 方式提交数据
    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        # 使用字典处理不同的注册方式
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email,

        }
    promise[form.type.data]()
    return 'success'

def __register_user_by_email():
    form = UserEmailForm(data=request.json)
    if form.validate():
        User.register_by_email(form.nickname.data,
                               form.secret.data,
                               form.account.data)


# @api.route('/register/by_mobile')
# def create_client():
#     pass
#
# @api.route('/register/by_wechart')
# def create_client():
#     pass