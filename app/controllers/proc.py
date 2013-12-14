#coding:utf-8

import json
import web
from config import render
<<<<<<< HEAD
from app.models import wtdata
=======
from app.models import wtdb
>>>>>>> 791d8beb9348769d137a51dc657431c01113a9fd


# watch tips in the given category
class watch:
    def GET(self, category):
<<<<<<< HEAD
        cur_tips = wtdata.getTips(category=category)
        if not cur_tips:
            cur_tips = wtdata.getDefaultTips()
=======
        cur_tips = wtdb.getTips(category=category)
        if not cur_tips:
            cur_tips = wtdb.getDefaultTips()
>>>>>>> 791d8beb9348769d137a51dc657431c01113a9fd

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

<<<<<<< HEAD
        cur_tips = wtdata.getTips(category=category)
        if not cur_tips:
            rdata['action'] = 'replace'
        new_tips_id = wtdata.addTips(new_tips)
=======
        cur_tips = wtdb.getTips(category=category)
        if not cur_tips:
            rdata['action'] = 'replace'
        new_tips_id = wtdb.addTips(new_tips)
>>>>>>> 791d8beb9348769d137a51dc657431c01113a9fd
        rdata['id'] = new_tips_id

        json_data = json.dumps(rdata)
        return json_data


# edit a tip
class edit:
    def POST(self):
        data = web.input()
        rdata = {'action': 'none'}
<<<<<<< HEAD
        updateSuccess = wtdata.updateTips(data)
=======
        updateSuccess = wtdb.updateTips(data)
>>>>>>> 791d8beb9348769d137a51dc657431c01113a9fd
        if updateSuccess:
            rdata['action'] = 'update'

        return json.dumps(rdata)


# delete a tip
class delete:
    def POST(self):
        data = web.input()
        category = data['category']

        rdata = {'action': 'none', 'default': json.dumps({})}
<<<<<<< HEAD
        deleteSuccess = wtdata.deleteTips(id=data['id'])
        if deleteSuccess:
            rdata['action'] = 'delete'

        tipsNum = wtdata.getTipsNum(category=category)
        if not tipsNum:
            default_tips = wtdata.getDefaultTips()
=======
        deleteSuccess = wtdb.deleteTips(id=data['id'])
        if deleteSuccess:
            rdata['action'] = 'delete'

        tipsNum = wtdb.getTipsNum(category=category)
        if not tipsNum:
            default_tips = wtdb.getDefaultTips()
>>>>>>> 791d8beb9348769d137a51dc657431c01113a9fd
            print '00'
            print (default_tips)
            rdata['default'] = json.dumps(default_tips)
            print rdata['default']
            print '--'

        return json.dumps(rdata)
