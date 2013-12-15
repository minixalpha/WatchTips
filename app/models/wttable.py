#coding: utf-8

from wtdb import db


class WTTable:
    """
    WatchTips Table
    """
    def __init__(self, tbname):
        self.tbname = tbname

    def add_item(self, idcolname=None, **values):
        item_id = db.insert(self.tbname, idcolname, **values)
        if idcolname:
            return item_id
        else:
            return None

    def update_item(self, where, **values):
        db.update(self.tbname, where, **values)

    def delete_item(self, where):
        db.delete(self.tbname, where)

    def search_item(self, columns, where):
        items = db.select(self.tbname, what=columns, where=where)
        return items

    def get_equal_condition(self, key, value):
        return str(key) + '="' + str(value) + '"'


class WTTipsTable(WTTable):
    def __init__(self, tbname):
        WTTable.__init__(self, tbname)
        self.id_col = 'tips_id'
        self.title_col = 'tips_title'
        self.content_col = 'tips_content'
        self.categoryid_col = 'category_id'

    def exist_tips(self, condition):
        cur_tips = self.search_item(
                columns='*',
                where=condition
                )
        if len(cur_tips):
            return True
        else:
            return False

    def delete_tips_by_id(self, tips_id):
        condition = self.get_equal_condition(self.id_col, tips_id)
        tips_is_exist = self.exist_tips(condition=condition)
        if tips_is_exist:
            self.delete_item(where=condition)
            return True
        else:
            return False

    def get_tips_by_category_id(self, category_id):
        condition = self.get_equal_condition(self.categoryid_col, category_id)
        tips = self.search_item(
                columns='*',
                where=condition
                )
        tips_list = []
        if tips:
            tips_list = list(tips)
        return tips_list

    def add_tips(self, new_tips):
        """
         new_tips: {'category_id':'X', 'title':'Y', 'content':'Z'}
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
    def __init__(self, tbname):
        WTTable.__init__(self, tbname)
        self.id_col = 'category_id'
        self.name_col = 'category_name'
        self.userid_col = 'user_id'

    def get_category_id_by_name(self, category_name):
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


tips = WTTipsTable('wt_tips')
category = WTCategoryTable('wt_category')
