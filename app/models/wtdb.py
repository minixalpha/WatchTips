#coding: utf-8

<<<<<<< HEAD
import web
import config


db = web.database(
        dbn=config.DATABASE_TYPE,
        db=config.DATABASE_NAME,
        user=config.DATABASE_USERNAME,
        pw=config.DATABASE_PASSWORD
        )
=======
from config import db


def getCategoryID(category='default'):
    category_ids = db.select(
        tables='wt_category',
        what='category_id',
        where='category_name="' + category + '"'
        )
    category_ids = list(category_ids)
    category_id = None
    if category_ids:
        category_id = category_ids[0]['category_id']
    return category_id


def getTips(category='default'):
    category_id = getCategoryID(category=category)
    cur_tips = []
    if category_id:
        cur_tips = db.select(
            'wt_tips',
            what='*',
            where='category_id="' + str(category_id) + '"'
            )
        cur_tips = list(cur_tips)
    return cur_tips


def getDefaultTips():
    return getTips(category='default')


def getLatestID(table_name, col_name):
    """
     Get Latest inserted item's ID

     Args:
         table_name: name of the table
         col_name: name of the id column

     Return:
         if add success, return the tip's id
         othewise return None
    """
    ids = db.select(
        table_name,
        what=col_name
        )
    ids = list(ids)

    max_id = None
    if ids:
        max_id = max([id[col_name] for id in ids])
    return max_id


def addTips(new_tips):
    """
     Add new tips

     Args:
         new_tips: {'category':'X', 'title':'Y', 'content':'Z'}

     Return:
         if add success, return new_tip's id
         othewise return None
    """
    category = new_tips['category']
    category_id = getCategoryID(category=category)
    tips_id = None

    db.insert(
        'wt_tips',
        tips_title=new_tips['title'],
        tips_content=new_tips['content'],
        category_id=category_id
        )
    tips_id = getLatestID('wt_tips', 'tips_id')

    return tips_id


def itemExist(tablename, col_name, value):
    items = db.select(
        tablename,
        what=col_name,
        where=col_name + '="' + str(value) + '"'
        )

    if items:
        return True
    else:
        return False


def updateTips(new_tips):
    """
     Update tips

     Args:
         new_tips: {'id':'X', 'title':'Y', 'content':'Z'}

     Return:
         if update success, return True
         othewise return False
    """
    id = new_tips['id']
    idExist = itemExist('wt_tips', 'tips_id', id)
    updateSuccess = False

    if idExist:
        db.update(
            'wt_tips',
            where='tips_id ="' + str(id) + '"',
            tips_title=new_tips['title'],
            tips_content=new_tips['content']
            )
        updateSuccess = True

    return updateSuccess


def deleteTips(id):
    idExist = itemExist('wt_tips', 'tips_id', id)
    deleteSuccess = False
    if idExist:
        db.delete(
            'wt_tips',
            where='tips_id="' + str(id) + '"'
            )
        deleteSuccess = True
    return deleteSuccess


def getItemsNum(tablename):
    items = db.select(tablename)
    items_num = len(items)

    return items_num


def getTipsNum(category):
    tips = getTips(category)
    tips_num = len(tips)
    return tips_num
>>>>>>> 791d8beb9348769d137a51dc657431c01113a9fd
