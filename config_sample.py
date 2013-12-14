#coding:utf-8

import web

render = web.template.render('app/views/', base='layout')
<<<<<<< HEAD

DATABASE_TYPE = 'mysql'
DATABASE_NAME = 'watchtips'
DATABASE_USERNAME = 'proj'
DATABASE_PASSWORD = 'XXX'
=======
db = web.database(dbn='mysql', db='watchtips', user='proj', pw='XXX')
>>>>>>> 791d8beb9348769d137a51dc657431c01113a9fd
