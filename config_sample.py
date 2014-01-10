#coding:utf-8


DEBUG = True
DATABASE_TYPE = 'mysql'
DATABASE_NAME = 'watchtips'
DATABASE_USERNAME = 'proj'
DATABASE_PASSWORD = 'XXX'

log_enable = True
log_file = 'log/wtlog.log'
log_tofile = True
log_toprint = True

ssl_enable = True
ssl_certificate_path = 'crtkey/server.crt'
ssl_private_key_path = 'crtkey/server.key'

sessionid_name = 'user_session'
session_dir = 'sessions'
