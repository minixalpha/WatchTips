#!/usr/bin/env python
#coding: utf-8

# User State Management

import web


def init_session(app, session_dir, sessionid_name,
        initializer={'ip': 0, 'agent': 0}):
    """
    Init sesstion, extend the original init process
    to make session shared by sub-app
    """
    web.config.session_parameters['cookie_name'] = sessionid_name
    store = web.session.DiskStore(session_dir)
    session = web.session.Session(app, store, initializer)

    # make session avaliable to share in sub-app
    def session_hook():
        web.ctx.session = session
    app.add_processor(web.loadhook(session_hook))

    return session


def get_session(key=None):
    if key == None:
        return web.ctx.session
    else:
        try:
            value = web.ctx.session.__getattribute__(key)
        except AttributeError:
            value = None
        return value


def set_session(key, value):
    web.ctx.session.__setattr__(key, value)


def clear_session():
    web.ctx.session.kill()
