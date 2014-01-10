#coding: utf-8

# Helper Functions about authority
from hashlib import sha256
from hmac import HMAC
import os
import web
from validate_email import validate_email as ve
import userstate


def validate_email(email_address):
    """
    Validate Whether Email Address is legal and exists


    Args:
        email_address: address of the email

    Return:
        if validate, return True
        otherwise return False
    """
    is_valid = ve(email_address)
    return is_valid


SALT_LENGTH = 8


def encrypt_info(info, salt=None, iteration=10):
    """
    Encrypt password

    Args:
        password: unicode string
        salt: random 64bits
        iteration: iteration times to HMAC

    Return:
        encrypted password with salt: unicode string
    """
    if not salt:
        salt = os.urandom(SALT_LENGTH)

    info = info.encode('UTF-8')

    result = info
    for i in range(iteration):
        result = HMAC(result, salt, sha256).digest()

    result = salt + result

    return result


def encrypt_password(password, salt=None, iteration=10):
    """
    Encrypt password

    Args:
        password: unicode string
        salt: random 64bits
        iteration: iteration times to HMAC

    Return:
        encrypted password with salt: unicode string
    """
    hashed_password = encrypt_info(password, salt, iteration)
    return hashed_password


def validate_info(hashed_info, info):
    """
    Validate whether current password is the same
    as hashed password

    if yes, return True
    otherwise return False
    """
    salt = hashed_info[:SALT_LENGTH]
    current_hashed_info = encrypt_info(info, salt=salt)
    return hashed_info == current_hashed_info


def validate_password(hashed_password, password):
    """
    Validate whether current password is the same
    as hashed password

    if yes, return True
    otherwise return False
    """
    is_validate = validate_info(hashed_password, password)
    return is_validate


def get_client_info():
    info = {}
    info['ip'] = web.ctx.ip
    info['agent'] = web.ctx.env.get('HTTP_USER_AGENT')
    return info


def set_login_state(username, userid):
    """
    Set login flag to current state
    """
    web.setcookie('user_name', username, secure=True, httponly=True)
    web.setcookie('logged_in', True, secure=True, httponly=True)

    client_info = get_client_info()
    userstate.set_session('ip', client_info['ip'])
    userstate.set_session('agent', client_info['agent'])
    userstate.set_session('userid', userid)


def clear_login_state():
    """
    Clear login state
    """
    userstate.clear_session()
    web.setcookie('user_name', '', expires=-1)
    web.setcookie('logged_in', False, expires=-1)
    web.setcookie('user_session', False, expires=-1)


def check_login_state():
    """
    If current user has logined in,
    return True,
    otherwise return False
    """
    username = web.cookies().get('user_name')
    if not username:
        return False

    logged_in = web.cookies().get('logged_in')
    if not logged_in:
        return False

    client_info = get_client_info()
    server_session = userstate.get_session()
    #server_ip = userstate.get_session('ip')
    #server_agent = userstate.get_session('agent')
    server_ip = server_session.ip
    server_agent = server_session.agent

    if not server_ip == client_info['ip']:
        return False

    if not server_agent == client_info['agent']:
        return False

    return True


def get_current_username():
    """
    Get current logged in username
    """
    username = web.cookies().get('user_name')
    return username


def get_current_userid():
    logged_in = check_login_state()
    if logged_in:
        server_session = userstate.get_session()
        userid = server_session.userid
        return userid
    else:
        return None
