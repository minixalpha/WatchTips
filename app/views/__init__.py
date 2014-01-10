#!/usr/bin/env python
#coding: utf-8

import web
import app.controllers.auth as auth
from app.models import wtdata

render = web.template.render('app/templates')


# Wrapper to get new state of layout
class Wrapper:
    def __init__(self):
        self.data = []

    def add_data(self, key, func):
        self.data.append((key, func))

    def __getattr__(self, attrname):
        if attrname == 'layout':
            globals = {}

            for (key, func) in self.data:
                globals[key] = func()

            layout = web.template.render(
                    'app/templates',
                    base='layout',
                    globals=globals)

            return layout
        else:
            raise AttributeError(attrname)


# layout wrappter to check something everytime
wrapper = Wrapper()


def is_login():
    loggedin = auth.check_login_state()
    return loggedin
wrapper.add_data('loggedin', is_login)


def get_current_categories():
    loggedin = auth.check_login_state()
    if loggedin:
        userid = auth.get_current_userid()
        categories = wtdata.get_all_categories(userid)
    else:
        categories = wtdata.get_super_categories()
    return categories
wrapper.add_data('categories', get_current_categories)
