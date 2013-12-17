#coding: utf-8

import wttable


def get_tips_by_category(category='default'):
    """
    Get tips in the given category

    Args:
        category: name of the category

    Return:
        tips in the given category, in the form:

        [
            {
                id_col: id_value, 
                title_col: title_value,
                content_col: content_value, 
            },
            ...
        ]
    """
    category_id = wttable.category.get_category_id_by_name(category)
    cur_tips = wttable.tips.get_tips_by_category_id(category_id)
    return cur_tips


def get_default_tips():
    """
    Get default tips, when the category has no tips

    Args:
        category: name of the category

    Return:
        tips in the given category, in the form:

        [
            {
                id_col: id_value, 
                title_col: title_value,
                content_col: content_value, 
            },
            ...
        ]
    """
    return get_tips_by_category(category='default')


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
    """
     Delete tips

     Args:
        id: id of the tips to be deleted

     Return:
         if delete success, return True
         othewise return False
    """
    delete_success = wttable.tips.delete_tips_by_id(id)
    return delete_success


def get_tips_count_by_category(category):
    """
     Get count of tips in the given category

     Args:
        category: name of the category

     Return:
        count of tips in the given category
    """
    category_id = wttable.category.get_category_id_by_name(category)
    tips_list = wttable.tips.get_tips_by_category_id(category_id)
    tips_count = len(tips_list)
    return tips_count
