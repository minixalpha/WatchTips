#coding:utf-8

import json
import web
from config import render
from app.models import wtdb


# watch tips in the given category
class watch:
    def GET(self, category):
        cur_tips = wtdb.getTips(category=category)
        if not cur_tips:
            cur_tips = wtdb.getDefaultTips()

        return render.watch(category, cur_tips)


#  add a new tip in the given category
class add:
    def POST(self):
        data = web.input()
        category = data['category']
        new_tips = {
                'category': category,
                'title': data['title'],
                'content': data['content']
                }
        rdata = {}
        rdata['action'] = "append"

        cur_tips = wtdb.getTips(category=category)
        if not cur_tips:
            rdata['action'] = 'replace'
        new_tips_id = wtdb.addTips(new_tips)
        rdata['id'] = new_tips_id

        json_data = json.dumps(rdata)
        return json_data


# edit a tip
class edit:
    def POST(self):
        data = web.input()
        rdata = {'action': 'none'}
        updateSuccess = wtdb.updateTips(data)
        if updateSuccess:
            rdata['action'] = 'update'

        return json.dumps(rdata)


# delete a tip
class delete:
    def POST(self):
        data = web.input()
        category = data['category']

        rdata = {'action': 'none', 'default': json.dumps({})}
        deleteSuccess = wtdb.deleteTips(id=data['id'])
        if deleteSuccess:
            rdata['action'] = 'delete'

        categoryNum = wtdb.getCategoryNum(category=category)
        if not categoryNum:
            rdata['default'] = json.dumps(wtdb.getDefaultTips())

        return json.dumps(rdata)
