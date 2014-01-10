#coding: utf-8

# media of tips module and wttable module

import wttable


def get_super_categories():
    categories = wttable.category.get_categories_by_userid(
            userid=1, exclude='default')
    return categories


def get_main_categories(userid):
    categories = wttable.category.get_categories_by_userid(
            userid=userid, exclude='default')
    return categories


def get_all_categories(userid):
    categories = wttable.category.get_categories_by_userid(userid=userid)
    return categories


def add_default_category(user_id):
    """
    Add default category which belongs to the user who has user_id

    Args:
        user_id: id of the user

    Return:
        category id
    """
    category_info = {
            'category_name': 'default',
            'category_img': 'default.png',
            'category_description': 'default category',
            'user_id': user_id
    }
    category_id = wttable.category.add_category(category_info)
    return category_id


def add_category(new_category):
    category_info = {
            'category_name': new_category['name'],
            'category_img': new_category['img'],
            'category_description': new_category['description'],
            'user_id': new_category['userid']
    }
    category_id = wttable.category.add_category(category_info)
    return category_id


def get_category_name_by_id(category_id):
    category_name = wttable.category.get_category_name_by_id(category_id)
    return category_name


def get_tips_by_category_id(category_id):
    """
    Get tips of the current user in the given category

    Args:
        username: name of current user
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
    cur_tips = wttable.tips.get_tips_by_category_id(category_id)
    return cur_tips


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
    tips_to_add = {}
    tips_to_add['category_id'] = new_tips['category']
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


def get_tips_count_by_category_id(category_id):
    """
     Get count of tips in the given category

     Args:
        category: name of the category

     Return:
        count of tips in the given category
    """
    category_id = int(category_id)
    tips_list = wttable.tips.get_tips_by_category_id(category_id)
    tips_count = len(tips_list)
    return tips_count


def add_user(user_info):
    """
    Add new user

    Args:
        user_info: {'username': X, 'password', Y, 'email', Z}

    Return:
        user id
    """
    user_id = wttable.user.add_user(user_info)
    return user_id


def exist_user(user_info):
    """
    Determine whether user exist or not

    Args:
        user_info: {'password', Y, 'email', Z}

    Return:
        if exist, return True
        otherwise return False
    """

    return wttable.user.exist_user(user_info)


def get_pwd_by_email(email):
    """
    Get password by email

    Args:
        email address

    Return:
        hashed password of the email's owner
    """
    return wttable.user.get_pwd_by_email(email)


def get_username_by_email(email):
    """
    Get username by email

    Args:
        email address

    Return:
        email owner's username
    """
    return wttable.user.get_username_by_email(email)


def get_userid_by_email(email):
    return wttable.user.get_userid_by_email(email)


def email_exist(email):
    return wttable.user.email_exist(email)


def is_category_owner(category_id, user_id):
    owner_id = wttable.category.get_userid_by_category_id(category_id)
    return owner_id == user_id
