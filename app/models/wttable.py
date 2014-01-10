#coding: utf-8

from wtdb import db


class WTTable:
    """
    WatchTips Table
    """
    def __init__(self, tbname):
        self.tbname = tbname

    def add_item(self, idcolname=None, **values):
        """
        Args:
            idcolname: column name of the new added item,
                if idcolname is not None, this function will
                return the value of this column, otherwise
                it will return None
            values: values to be added in to the database
        """
        item_id = db.insert(self.tbname, idcolname, **values)
        if idcolname:
            return item_id
        else:
            return None

    def update_item(self, where, **values):
        """
        Update an item in a condition, with new value
        """
        db.update(self.tbname, where, **values)

    def delete_item(self, where):
        """
        Delete items in a condition
        """
        db.delete(self.tbname, where)

    def search_item(self, columns, where):
        """
        Return items of the given columns and condition
        """
        items = db.select(self.tbname, what=columns, where=where)
        return items

    def get_equal_condition(self, key, value):
        """
        Get equal condition which is used for search items
        """
        equal_codition = str(key) + '="' + str(value) + '"'
        return equal_codition

    def combine_columns(self, *args):
        """
        Get columns list

        Args:
            variable arguments list: eg: combine_columns('id', 'title')

        Return:
            columns in a fix form
        """
        columns = []
        for arg in args:
            columns.append(arg)
        return ','.join(columns)


class WTTipsTable(WTTable):
    """
    Watch Tips talbe: wt_tips
    """
    # init the column name, must in consist with
    # the definition of 'wt_tips' table in schemal.sql
    def __init__(self):
        WTTable.__init__(self, 'wt_tips')
        self.id_col = 'tips_id'
        self.title_col = 'tips_title'
        self.content_col = 'tips_content'
        self.categoryid_col = 'category_id'

    def exist_tips(self, condition):
        """
        Detemine whether a tips is exist in a given condition or not

        Args:
            condition: in the form 'a = "a_value"'

        Return:
            True if exist, otherwise False
        """
        cur_tips = self.search_item(columns='*', where=condition)
        if len(cur_tips):
            return True
        else:
            return False

    def delete_tips_by_id(self, tips_id):
        """
        Delete tips by tips id

        Args:

        Return:
        """
        condition = self.get_equal_condition(self.id_col, tips_id)
        tips_is_exist = self.exist_tips(condition=condition)
        if tips_is_exist:
            self.delete_item(where=condition)
            return True
        else:
            return False

    def get_tips_by_category_id(self, category_id):
        """
        Get tips_list by the given category id,

        tips_list:
        [
            {
                self.id_col: id_value,
                self.title_col: title_value,
                self.content_col: content_value,
            },
            ...
        ]
        """
        if not category_id:
            return []
        condition = self.get_equal_condition(self.categoryid_col, category_id)
        columns = self.combine_columns(
                self.id_col,
                self.title_col,
                self.content_col)
        tips = self.search_item(
                columns=columns,
                where=condition
                )
        tips_list = []
        if tips:
            tips_list = list(tips)
        return tips_list

    def add_tips(self, new_tips):
        """
        Add new tips

        Args:
            new_tips: {'category_id':'X', 'title':'Y', 'content':'Z'}

        Return value:
            id of the new tips
        """
        values = {
                self.categoryid_col: new_tips['category_id'],
                self.title_col: new_tips['title'],
                self.content_col: new_tips['content']
                }

        tips_id = self.add_item(self.id_col, **values)
        return tips_id

    def update_tips(self, updated_tips):
        """
        Args:
            updated: {'id':'X', 'title':'Y', 'content':'Z'}

        Return value:
            if update success, return True, otherwise False
        """
        exist_condition = self.get_equal_condition(
                self.id_col, updated_tips['id'])
        tips_is_exist = self.exist_tips(exist_condition)

        if tips_is_exist:
            values = {
                    self.title_col: updated_tips['title'],
                    self.content_col: updated_tips['content']
                    }
            update_condition = self.get_equal_condition(
                    self.id_col, updated_tips['id'])
            self.update_item(
                    where=update_condition,
                    **values
                    )
            return True
        else:
            return False


class WTCategoryTable(WTTable):
    """
    Watch Tips table: wt_category
    """
    # init the column name, must in consist with
    # the definition of 'wt_category' table in schemal.sql
    def __init__(self):
        WTTable.__init__(self, 'wt_category')
        self.id_col = 'category_id'
        self.name_col = 'category_name'
        self.img_col = 'category_img'
        self.description_col = 'category_description'
        self.userid_col = 'user_id'

    def get_info_by_key(self, info_col, key_col, key_value):
        search_condition = self.get_equal_condition(key_col, key_value)
        info = self.search_item(columns=info_col, where=search_condition)
        info_list = []
        if info:
            info_list = list(info)
        return info_list

    def get_unique_info_by_key(self, info_col, key_col, key_value):
        info_list = self.get_info_by_key(info_col, key_col, key_value)
        if info_list:
            info = info_list[0][info_col]
        else:
            info = None
        return info

    def get_category_name_by_id(self, category_id):
        category_name = self.get_unique_info_by_key(
                self.name_col, self.id_col, category_id)
        return category_name

    def get_userid_by_category_id(self, category_id):
        user_id = self.get_unique_info_by_key(
                self.userid_col, self.id_col, category_id)
        return user_id

    def get_category_id_by_name(self, category_name):
        category_id = self.get_unique_info_by_key(
                self.id_col, self.name_col, category_name)
        return category_id

    def get_categories_by_userid(self, userid, exclude=None):
        categories = self.get_info_by_key('*', self.userid_col, userid)
        if exclude:
            categories_except_default = [
                    category for category in categories
                    if not category[self.name_col] == exclude
                    ]
            return categories_except_default
        else:
            return categories

    def add_category(self, category_info):
        """
        Args:
            category_info: {
                'category_name':X, 'category_img': Y,
                'category_description':Z, 'user_id':Q }

        Return:
            new category id
        """
        new_category = {
                self.name_col: category_info['category_name'],
                self.img_col: category_info['category_img'],
                self.description_col: category_info['category_description'],
                self.userid_col: category_info['user_id']
        }
        category_id = self.add_item(idcolname=self.id_col, **new_category)
        return category_id


class WTUserTable(WTTable):
    """
    Watch Tips table: wt_user
    """
    def __init__(self):
        WTTable.__init__(self, 'wt_user')
        self.id_col = 'user_id'
        self.name_col = 'user_name'
        self.email_col = 'user_email'
        self.pwd_col = 'user_password'

    def email_exist(self, email):
        email_condition = self.get_equal_condition(self.email_col, email)
        users = self.search_item(columns=self.email_col, where=email_condition)
        if not users:
            return False
        else:
            return True

    def add_user(self, user_info):
        """
        Args:
            user_info: {'username': X, 'password', Y, 'email', Z}

        Return:
            new user id
        """
        new_user = {
                self.name_col: user_info['username'],
                self.email_col: user_info['email'],
                self.pwd_col: user_info['password']
                }
        user_id = self.add_item(idcolname=self.id_col, **new_user)
        return user_id

    def get_info_by_email(self, col_name, email):
        """
        Get information of a column by email

        Args:
            col_name: column name of the user table
            email: email address

        Return:
            information of the given column by email
        """
        email_condition = self.get_equal_condition(
                self.email_col,
                email)
        users = self.search_item(columns=col_name, where=email_condition)
        if not users:
            return None
        else:
            return users[0][col_name]

    def get_pwd_by_email(self, email):
        """
        Args:
            email address

        Return:
            hashed password of the email's owner
        """
        return self.get_info_by_email(self.pwd_col, email)

    def get_username_by_email(self, email):
        """
        Args:
            email address

        Return:
            email owner's username
        """
        return self.get_info_by_email(self.name_col, email)

    def get_userid_by_email(self, email):
        return self.get_info_by_email(self.id_col, email)

    def exist_user(self, user_info):
        """
        Determine whether user exist or not

        Args:
            user_info: {'password', Y, 'email', Z}

        Return:
            if exist, return True
            otherwise return False
        """
        email_condition = self.get_equal_condition(
                self.email_col,
                user_info['email'])
        pwd_condition = self.get_equal_condition(
                self.pwd_col,
                user_info['password'])
        condition = email_condition + ' and ' + pwd_condition
        users = self.search_item(columns=self.name_col, where=condition)

        if len(users):
            return True
        else:
            return False


tips = WTTipsTable()
category = WTCategoryTable()
user = WTUserTable()
