#coding: utf-8

import wttable


def get_category_id(category='default'):
    category_id = wttable.category.get_category_id_by_name(category)
    return category_id


def get_tips(category='default'):
    category_id = wttable.category.get_category_id_by_name(category)
    cur_tips = wttable.tips.get_tips_by_category_id(category_id)
    return cur_tips


def get_default_tips():
    return get_tips(category='default')


def add_tips(new_tips):
    """
     Add new tips

     Args:
         new_tips: {'category':'X', 'title':'Y', 'content':'Z'}

     Return:
         if add success, return new_tip's id
         othewise return None
    """
    category_id = wttable.category.get_category_id_by_name(
            new_tips['category'])
    tips_to_add = {}
    tips_to_add['category_id'] = category_id
    tips_to_add['title'] = new_tips['title']
    tips_to_add['content'] = new_tips['content']
    tips_id = wttable.tips.add_tips(tips_to_add)

    return tips_id


def update_tips(tips_to_update):
    """
     Update tips

     Args:
         updated_tips: {'id':'X', 'title':'Y', 'content':'Z'}

     Return:
         if update success, return True
         othewise return False
    """
    update_success = wttable.tips.update_tips(tips_to_update)

    return update_success


def delete_tips(id):
    delete_success = wttable.tips.delete_tips_by_id(id)
    return delete_success


def get_tips_count(category):
    category_id = wttable.category.get_category_id_by_name(category)
    tips_list = wttable.tips.get_tips_by_category_id(category_id)
    tips_count = len(tips_list)
    return tips_count
