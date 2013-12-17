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

    def get_columns(self, *args):
        """
        Get columns list

        Args:
            variable arguments list: eg: get_columns('id', 'title')

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
        cur_tips = self.search_item(
                columns='*',
                where=condition
                )
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
        condition = self.get_equal_condition(self.categoryid_col, category_id)
        columns = self.get_columns(self.id_col, self.title_col, self.content_col)
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

        tips_id = self.add_item(
                self.id_col,
                **values
                )
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
    Watch Tips talbe: wt_category
    """
    # init the column name, must in consist with
    # the definition of 'wt_category' table in schemal.sql
    def __init__(self):
        WTTable.__init__(self, 'wt_category')
        self.id_col = 'category_id'
        self.name_col = 'category_name'
        self.userid_col = 'user_id'

    def get_category_id_by_name(self, category_name):
        """
        Get category id by category name
        
        Args:
            category_name: name of the category

        Return:
            category id of the given category name
        """
        search_condition = self.get_equal_condition(
                self.name_col, category_name)
        ids = self.search_item(
            columns=self.id_col,
            where=search_condition
            )
        idlist = []
        if ids:
            idlist = list(ids)

        if idlist:
            category_id = idlist[0][self.id_col]
        return category_id


tips = WTTipsTable()
category = WTCategoryTable()
