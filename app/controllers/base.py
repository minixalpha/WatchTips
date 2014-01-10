#coding:utf-8

import web
from app.views import wrapper as views
from app.views import render
from app.models import wtdata
from app.controllers import auth


class index:
    def GET(self):
        categories = wtdata.get_super_categories()
        currrent_userid = auth.get_current_userid()
        if str(currrent_userid) == str(1):
            is_owner = True
        else:
            is_owner = False
        return views.layout.index(categories=categories, is_owner=is_owner)


class home:
    def GET(self, userid):
        categories = wtdata.get_main_categories(userid=int(userid))
        currrent_userid = auth.get_current_userid()
        if str(currrent_userid) == str(userid):
            is_owner = True
        else:
            is_owner = False
        return views.layout.index(categories=categories, is_owner=is_owner)


def notfound():
    #return web.notfound("No Tips Here")
    return web.notfound(render.notfound())
