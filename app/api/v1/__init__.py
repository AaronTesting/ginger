# -*- coding: utf-8 -*-
__author__ = 'Aaron'
__date__ = '2020/4/1 0001 17:03'


from flask import Blueprint
from app.api.v1 import user, client
from app.api.v1 import book


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    # user.api.register(bp_v1)
    # book.api.register(bp_v1)
    client.api.register(bp_v1)
    return bp_v1