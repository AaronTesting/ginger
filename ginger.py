# -*- coding: utf-8 -*-
__author__ = 'Aaron'
__date__ = '2020/4/1 0001 16:06'


from app.app import create_app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)