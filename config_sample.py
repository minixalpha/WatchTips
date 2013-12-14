#coding:utf-8

import web

render = web.template.render('app/views/', base='layout')

DATABASE_TYPE = 'mysql'
DATABASE_NAME = 'watchtips'
DATABASE_USERNAME = 'proj'
DATABASE_PASSWORD = 'XXX'
