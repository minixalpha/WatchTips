#coding:utf-8

import json
import web
from config import render
from app.models import wtdata


# watch tips in the given category
class watch:
    def GET(self, category):
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
        cur_tips = wtdata.get_tips_by_category(category=category)
        if not cur_tips:
            cur_tips = wtdata.get_default_tips()

        return render.watch(category, cur_tips)


#  add a new tip in the given category
class add:
    def POST(self):
        """
        Add new tips

        Args:
            inexplicit args in web.input()
            in the form:
            {
                'category': category_value
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
        """
        data = web.input()
        category = data['category']
        new_tips = {
                'category': category,
                'title': data['title'],
                'content': data['content']
                }
        rdata = {}
        rdata['action'] = 'append'

        cur_tips = wtdata.get_tips_by_category(category=category)
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
            'category': category_value
            'title': title_value
            'content'" content_value
        }

    Return:
        a jason form data:
            '{"action": "none"}' : no action need to do

            or

            '{"action": "update"}': update current tips
    """
    def POST(self):
        data = web.input()
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
            'id': id_value
            'category': category_value
        }

    Return:
        a jason form data:
            '{"action": "none"}' : no action need to do

            or

            '{"action": "delete"}': delete tips which has 'id_value'
    """
    def POST(self):
        data = web.input()
        category = data['category']

        rdata = {'action': 'none', 'default': json.dumps({})}
        delete_success = wtdata.delete_tips(id=data['id'])
        if delete_success:
            rdata['action'] = 'delete'

        tips_count = wtdata.get_tips_count_by_category(category=category)
        if not tips_count:
            default_tips = wtdata.get_default_tips()
            rdata['default'] = json.dumps(default_tips)

        return json.dumps(rdata)
