#coding:utf-8

from config import render


class index:
    def GET(self):
        return render.index()
