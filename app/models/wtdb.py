#coding: utf-8

import web
import config


db = web.database(
        dbn=config.DATABASE_TYPE,
        db=config.DATABASE_NAME,
        user=config.DATABASE_USERNAME,
        pw=config.DATABASE_PASSWORD
        )
