#coding: utf-8

import wttable


def getCategoryID(category='default'):
    category_id = wttable.category.getCategoryIDByName(category)
    return category_id


def getTips(category='default'):
    category_id = wttable.category.getCategoryIDByName(category)
    cur_tips = wttable.tips.getTipsByCategoryID(category_id)
    return cur_tips


def getDefaultTips():
    return getTips(category='default')


def addTips(new_tips):
    """
     Add new tips

     Args:
         new_tips: {'category':'X', 'title':'Y', 'content':'Z'}

     Return:
         if add success, return new_tip's id
         othewise return None
    """
    category_id = wttable.category.getCategoryIDByName(new_tips['category'])
    add_tips = {}
    add_tips['category_id'] = category_id
    add_tips['title'] = new_tips['title']
    add_tips['content'] = new_tips['content']
    tips_id = wttable.tips.addTips(add_tips)

    return tips_id


def updateTips(updated_tips):
    """
     Update tips

     Args:
         updated_tips: {'id':'X', 'title':'Y', 'content':'Z'}

     Return:
         if update success, return True
         othewise return False
    """
    updateSuccess = wttable.tips.updateTips(updated_tips)

    return updateSuccess


def deleteTips(id):
    deleteSuccess = wttable.tips.deleteTipsByID(id)
    return deleteSuccess


def getTipsNum(category):
    category_id = wttable.category.getCategoryIDByName(category)
    tips_list = wttable.tips.getTipsByCategoryID(category_id)
    tips_num = len(tips_list)
    return tips_num
