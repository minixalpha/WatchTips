#!/usr/bin/env python
#coding: utf-8

# category: add

import json
import web
from app.models import wtdata
import auth


#  add a new tip in the given category
class add:
    def POST(self):
        """
        Add new category

        Args:
            inexplicit args in web.input()
            in the form:
            {
                'name': category_name
                'description': description
            }

        Return:
            a jason form data:
                '{
                    "action": "append",
                    "id": category_id,
                    "img": category_img,
                    "description" category_description
                 }' :
                append new category

                or

                '{"action": "illegal"}': illegal operation
        """

        logined = auth.check_login_state()
        if not logined:
            return json.dumps({'action': 'illegal'})

        data = web.input()

        userid = auth.get_current_userid()
        new_category = {
                'name': data['name'],
                'description': data['description'],
                'img': 'default.png',
                'userid': userid
                }
        new_category_id = wtdata.add_category(new_category)

        rdata = {}
        rdata['action'] = 'append'
        rdata['id'] = new_category_id
        rdata['img'] = 'default.png'
        rdata['description'] = data['description']

        json_data = json.dumps(rdata)
        return json_data
