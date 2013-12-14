#coding: utf-8

from wtdb import db

class WTTable:
    def __init__(self, tbname):
        self.tbname = tbname

    def addItem(self, idcolname=None, **values):
        id = db.insert(self.tbname, idcolname, **values)
        if idcolname:
            return id
        else:
            return None

    def updateItem(self, where, **values):
        db.update(self.tbname, where, **values)

    def deleteItem(self, where):
        db.delete(self.tbname, where)

    def searchItem(self, columns, where):
        items = db.select(self.tbname, what=columns, where=where)
        return items


class WTTipsTable(WTTable):
    def __init__(self, tbname):
        WTTable.__init__(self, tbname)
        self.id_col = 'tips_id'
        self.title_col = 'tips_title'
        self.content_col = 'tips_content'
        self.categoryid_col = 'category_id'
    
    def existTips(self, where):
        cur_tips = self.searchItem(
                columns='*',
                where=where
                )
        if len(cur_tips):
            tips_Exist = True
        else:
            tips_Exist = False
        return tips_Exist

    def deleteTipsByID(self, id):
        condition = self.id_col + '="' + str(id) + '"'
        exist_tips = self.existTips(where = condition)
        deleteSuccess = False
        if exist_tips:
            self.deleteItem(where = condition)
            deleteSuccess = True
        return deleteSuccess

    def getTipsByCategoryID(self, category_id):
        tips = self.searchItem(
                columns='*',
                where=self.categoryid_col + '="' + str(category_id) +'"'
                )
        tips_list = []
        if tips:
            tips_list = list(tips)
        return tips_list

    def addTips(self, new_tips):
        """
         new_tips: {'category_id':'X', 'title':'Y', 'content':'Z'}
        """
        values = {
                self.categoryid_col : new_tips['category_id'],
                self.title_col : new_tips['title'],
                self.content_col : new_tips['content']
                }

        id = self.addItem(
                self.id_col,
                **values
                )
        return id

    def updateTips(self, updated_tips):
        """
        Args:
            updated: {'id':'X', 'title':'Y', 'content':'Z'}
        """
        exist_tips = self.existTips(
                self.id_col + '="' + str(updated_tips['id']) + '"')

        updateSuccess = False
        if exist_tips:
            values = {
                    self.title_col : updated_tips['title'],
                    self.content_col : updated_tips['content']
                    }
            self.updateItem(
                    where=self.id_col + '="' + str(updated_tips['id']) + '"',
                    **values
                    )
            updateSuccess = True
        return updateSuccess


class WTCategoryTable(WTTable):
    def __init__(self, tbname):
        WTTable.__init__(self, tbname)
        self.id_col = 'category_id'
        self.name_col = 'category_name'
        self.userid_col = 'user_id'

    def getCategoryIDByName(self, category_name):
        ids = self.searchItem(
            columns=self.id_col,
            where=self.name_col + '="' + str(category_name) + '"'
            )
        idlist = []
        if ids:
            idlist = list(ids)
        
        id = None
        if idlist:
            id = idlist[0][self.id_col]
        return id


tips = WTTipsTable('wt_tips')
category = WTCategoryTable('wt_category')
