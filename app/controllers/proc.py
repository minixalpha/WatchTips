#coding:utf-8

import json
import web
from config import render


# tips used to test before using database
tips = {}
tips['default'] = [
        {
            'id':0,
            'title':'',
            'content':'Add your tips'
        },
        {
            'id':1,
            'title':'',
            'content':'Watch your tips'
        },
        {
            'id':2,
            'title':'',
            'content':'Forget your tips'
        }]
tips['python'] = [
        {
            'id':3,
            'title':'import this',
            'content':'Beautiful is better than ugly,'
            'Explicit is better than implicit'
        },
        {
            'id':4,
            'title':'import that',
            'content':'Beautiful is better than ugly,'
            'Explicit is better than implicit'
        }]
tips['javascript'] = tips['default']
tips['html5'] = tips['default']
tiplen = 5


# watch tips in the given category
class watch:
    def GET(self, category):
        cur_tips = tips.get(category)
        if not cur_tips:
            cur_tips = tips['default']
        return render.watch(category, cur_tips)


#  add a new tip in the given category
class add:
    def POST(self):
        global tiplen
        data = web.input()
        category = data['category']
        print(tiplen)
        new_tips = {
                'id': tiplen,
                'title': data['title'],
                'content': data['content']
                }
        rdata = {}
        rdata['id'] = tiplen
        rdata['action'] = "append"
        if tips[category] == tips['default']:
            tips[category] = []
            rdata['action'] = "replace"
        tips[category].append(new_tips)
        tiplen += 1
        json_data = json.dumps(rdata)
        return json_data


# edit a tip
class edit:
    def POST(self):
        data = web.input()
        category = data['category']
        id = data['id']
        title = data['title']
        content = data['content']

        cur_tips = tips.get(category, [])
        rdata = {'action':'none'}
        if not cur_tips == tips['default']:
            for tip in cur_tips:
                if tip['id'] == int(id):
                    tip['title'] = title
                    tip['content'] = content
                    rdata['action'] = 'update'
        return json.dumps(rdata)


# delete a tip
class delete:
    def POST(self):
        data = web.input()
        category = data['category']
        id = data['id']

        cur_tips = tips.get(category, [])
        rdata = {'action':'none', 'default':json.dumps({})}
        if not cur_tips == tips['default']:
            for tip in cur_tips:
                if tip['id'] == int(id):
                    cur_tips.remove(tip)
                    rdata['action'] = 'delete'
                    if not cur_tips:
                        rdata['default'] = json.dumps(tips['default'])
                        tips[category] = tips['default']
                    break
        return json.dumps(rdata)
