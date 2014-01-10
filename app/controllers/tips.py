#coding:utf-8

# tips: watch, add, edit, delete

import json
import web
from app.views import wrapper as views
from app.models import wtdata
import auth
import redirect


# watch tips in the given category
class watch:
    def GET(self, category_id):
        """
        Process the request for /watch/$category

        Args:
            category: value of $category

        Return:
            category: current category
            cur_tips: tips in the current category in the form
                [
                    {
                        self.id_col: id_value,
                        self.title_col: title_value,
                        self.content_col: content_value,
                    },
                    ...
                ]
        """
        logined = auth.check_login_state()
        if not logined:
            cur_tips = wtdata.get_default_tips()
            category_name = wtdata.get_category_name_by_id(category_id)
        else:
            cur_tips = wtdata.get_tips_by_category_id(category_id)
            category_name = wtdata.get_category_name_by_id(category_id)
            if not cur_tips:
                cur_tips = wtdata.get_default_tips()

        return views.layout.watch(category_id, category_name, cur_tips)


#  add a new tip in the given category
class add:
    def POST(self):
        """
        Add new tips

        Args:
            inexplicit args in web.input()
            in the form:
            {
                'category': category_id
                'title': title_value
                'content'" content_value
            }

        Return:
            a jason form data:
                '{"action": "append", "id": id_value}' : append new tips in
                the current category

                or

                '{"action": "replace", "id": id_value}': replace the default
                tips in the current category

                or

                '{"action": "login"}': prompt user to login

                or

                '{"action": "illegal"}': illegal operation
        """

        logined = auth.check_login_state()
        if not logined:
            return json.dumps({'action': 'login'})

        data = web.input()

        category_id = data['category']
        user_id = auth.get_current_userid()
        is_owner = wtdata.is_category_owner(category_id, user_id)
        if not is_owner:
            return json.dumps({'action': 'illegal'})

        new_tips = {
                'category': category_id,
                'title': data['title'],
                'content': data['content']
                }
        rdata = {}
        rdata['action'] = 'append'

        cur_tips = wtdata.get_tips_by_category_id(category_id=int(category_id))
        if not cur_tips:
            rdata['action'] = 'replace'
        new_tips_id = wtdata.add_tips(new_tips)
        rdata['id'] = new_tips_id

        json_data = json.dumps(rdata)
        return json_data


# edit a tip
class edit:
    """
    Edit new tips

    Args:
        inexplicit args in web.input()
        in the form:
        {
            'id': id_value
            'category': category_id
            'title': title_value
            'content'" content_value
        }

    Return:
        a jason form data:
            '{"action": "none"}' : no action need to do

            or

            '{"action": "update"}': update current tips

            or

            '{"action": "login"}': prompt user to login

            or

            '{"action": "illegal"}': illegal operation
    """
    def POST(self):
        logined = auth.check_login_state()
        if not logined:
            return redirect.login()

        data = web.input()
        category_id = int(data['category'])
        user_id = auth.get_current_userid()
        is_owner = wtdata.is_category_owner(category_id, user_id)
        if not is_owner:
            return json.dumps({'action': 'illegal'})

        rdata = {'action': 'none'}
        update_success = wtdata.update_tips(data)
        if update_success:
            rdata['action'] = 'update'

        return json.dumps(rdata)


# delete a tip
class delete:
    """
    Delete tips

    Args:
        inexplicit args in web.input()
        in the form:
        {
            'id': tips_id
            'category': category_id
        }

    Return:
        a jason form data:
            '{"action": "none"}' : no action need to do

            or

            '{"action": "delete"}': delete tips which has 'id_value'

            or

            '{"action": "login"}': prompt user to login

            or

            '{"action": "illegal"}': illegal operation
    """
    def POST(self):
        logined = auth.check_login_state()
        if not logined:
            return redirect.login()

        data = web.input()
        category_id = data['category']
        user_id = auth.get_current_userid()
        is_owner = wtdata.is_category_owner(category_id, user_id)
        if not is_owner:
            return json.dumps({'action': 'illegal'})

        rdata = {'action': 'none', 'default': json.dumps({})}
        delete_success = wtdata.delete_tips(id=data['id'])
        if delete_success:
            rdata['action'] = 'delete'

        tips_count = wtdata.get_tips_count_by_category_id(
                category_id=category_id)
        if not tips_count:
            default_tips = wtdata.get_default_tips()
            rdata['default'] = json.dumps(default_tips)

        return json.dumps(rdata)
