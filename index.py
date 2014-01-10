#coding:utf-8

import web
from app.controllers import userstate
from app.controllers.base import notfound
from app.wtserver import wtlog
from app.wtserver import wtssl
import config


web.config.debug = False
wtssl.enable_ssl(config.ssl_enable)

urls = (
        "/", "app.controllers.base.index",
        "/home/(.+)", "app.controllers.base.home",
        "/watch/(.+)", "app.controllers.tips.watch",
        "/add", "app.controllers.tips.add",
        "/edit", "app.controllers.tips.edit",
        "/delete", "app.controllers.tips.delete",
        "/addCategory", "app.controllers.category.add",
        "/register", "app.controllers.user.register",
        "/login", "app.controllers.user.login",
        "/logout", "app.controllers.user.logout",
        )

app = web.application(urls, globals(), autoreload=True)
app.notfound = notfound
session = userstate.init_session(
        app, config.session_dir, config.sessionid_name)


if __name__ == "__main__":
    if config.log_enable:
        app.run(wtlog.Log)
    else:
        app.run()
