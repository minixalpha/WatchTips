#coding: utf-8

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
tips['javascript'] = []
tips['html5'] = []
tiplen = 5


def getTips(category='default'):
    cur_tips = tips.get(category)
    return cur_tips


def getDefaultTips():
    return tips['default']


def addTips(new_tips):
    global tiplen
    category = new_tips['category']
    tiplen += 1
    tip = {}
    tip['id'] = tiplen
    tip['title'] = new_tips['title']
    tip['content'] = new_tips['content']

    tips[category].append(tip)
    return tiplen


def updateTips(new_tips):
    print(new_tips)
    id = new_tips['id']
    title = new_tips['title']
    content = new_tips['content']

    for category in tips:
        for tip in tips[category]:
            if tip['id'] == int(id):
                if not category == 'default':
                    tip['title'] = title
                    tip['content'] = content
                    return True
                break
    return False


def deleteTips(id):
    for category in tips:
        for tip in tips[category]:
            if tip['id'] == int(id):
                if not category == 'default':
                    tips[category].remove(tip)
                    return True
                break
    return False


def getCategoryNum(category):
    return len(tips[category])
