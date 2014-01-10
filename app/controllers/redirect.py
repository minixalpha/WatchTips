#!/usr/bin/env python
#coding: utf-8

import json

# Redirect action command to client


# Redirect to login page
def login():
    return json.dumps({'action': 'login'})


# Redirect to register page
def register():
    return json.dumps({'action': 'register'})
