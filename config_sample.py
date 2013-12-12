#coding:utf-8

import web

render = web.template.render('app/views/', base='layout')
db = web.database(dbn='mysql', db='watchtips', user='proj', pw='XXX')
