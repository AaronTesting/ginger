# -*- coding: utf-8 -*-
__author__ = 'Aaron'
__date__ = '2020/4/1 0001 20:29'

from enum import Enum


class ClientTypeEnum(Enum):
    # register type
    USER_EMAIL = 100
    USER_MOBILE = 101
    USER_MINA = 200
    USER_WX = 201