#coding:utf-8

import web
import app

urls = (
        "/", "app.controllers.base.index",
        "/watch/(.+)", "app.controllers.proc.watch",
        "/add", "app.controllers.proc.add",
        "/edit", "app.controllers.proc.edit",
        "/delete", "app.controllers.proc.delete"
        )
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
