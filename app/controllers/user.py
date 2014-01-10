#coding:utf-8

# User Management

import web
import auth
from app.views import wrapper as views
from app.models import wtdata
import config


class register:
    def GET(self):
        return views.layout.register(info='')

    def POST(self):
        """
        Posted data has three keys:
            'username', 'email', 'password'
        """
        data = web.input()

        email = data['email']
        email_validate = auth.validate_email(email)
        if not email_validate:
            return views.layout.register(info='email can not be validate')
        email_exist = wtdata.email_exist(email)
        if email_exist:
            return views.layout.register(info='email exist')

        pwd = data['password']
        hashed_pwd = auth.encrypt_password(pwd)
        print(hashed_pwd)

        user_info = {}
        user_info['username'] = data['username']
        user_info['password'] = hashed_pwd
        user_info['email'] = email
        user_id = wtdata.add_user(user_info)
        wtdata.add_default_category(user_id)

        return web.seeother('/login')


class login:
    def GET(self):
        return views.layout.login(info='')

    def POST(self):
        data = web.input()
        data = web.input()

        email = data['email']
        if not config.DEBUG:
            email_validate = auth.validate_email(email)
            if not email_validate:
                return 'email is not validate'

        pwd = data['password']
        hashed_pwd = wtdata.get_pwd_by_email(email)
        if hashed_pwd:
            login_success = auth.validate_password(hashed_pwd, pwd)
        else:
            login_success = False

        if login_success:
            username = wtdata.get_username_by_email(email)
            userid = wtdata.get_userid_by_email(email)
            auth.set_login_state(username, userid)
            return web.seeother('/home/' + str(userid))
        else:
            return views.layout.login(info='Username or Password is Wrong')


class logout:
    def GET(self):
        auth.clear_login_state()
        return web.seeother('/')
