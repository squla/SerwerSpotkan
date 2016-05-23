import gtk
from sqlalchemy.orm import sessionmaker
from Model.table_def import User
import Dialog
import datetime


class ActivityController:
    def __init__(self, wTree, view, user, session):
        self.wTree = wTree
        self.user = user
        self.view = view
        self.session = session
        self.initButton()
        self.refresh()

    def refresh(self, today=False, lista=None):

        if lista is None:
            lista = self.user.activities_list
        self.view.treeList.clear()
        for i in lista:
            if not today or today and i.day == datetime.datetime.now().date():
                self.view.treeList.append(i.getList(True))

    def initButton(self):
        dic = {"on_addButton": self.add,
               "on_deleteButton": self.delete,
               "on_editButton": self.edit,
               "on_findButton": self.find,
               "on_todayButton": self.today,
               "on_reloadButton": self.reload
               }
        self.wTree.signal_autoconnect(dic)

    def add(self, widget):
        print "add"
        dialog = Dialog.AddActivityDialog(self.wTree)
        result, activity = dialog.run()
        if (result == 1):
            print "dodanie" + activity.name
            self.user.activities_list.append(activity)
            self.session.add(activity)
            self.session.commit()
            self.refresh()

    def delete(self, widget):
        dialog = Dialog.RemoveActivityDialog(self.wTree)
        name, day, start, stop = dialog.run()
        for i in self.user.activities_list:
            list = i.getList(True)
            if (name == list[0] and day == list[1] and
                        start == list[2] and stop == list[3]):
                self.session.delete(i)
                self.session.commit()
                self.session.expire_all()
                self.refresh()
        print "delete"

    def getObject(self):
        treeView = self.view.treeView
        selection = treeView.get_selection()
        (model, path) = selection.get_selected_rows()
        tree_iter = model.get_iter(path[0])
        for i in self.user.activities_list:
            list = i.getList(True)
            if (model.get_value(tree_iter, 0) == list[0] and model.get_value(tree_iter, 1) == list[1] and
                        model.get_value(tree_iter, 2) == list[2] and model.get_value(tree_iter, 3) == list[3]):
                return i

    def edit(self, widget):
        dialog = Dialog.EditActivityDialog(self.getObject())
        result, activity = dialog.run()
        if (result == 1):
            self.session.add(activity)
            self.session.commit()
            self.refresh()
        print "edit"

    def find(self, widget):
        print "find"
        dialog = Dialog.FindActivityDialog()
        result, list = dialog.run()
        new_list = []
        if (result == 1):
            for i in self.user.activities_list:
                if (list[0] is None or i.name == list[0]) \
                        and (list[1] is None or i.day == list[1]) \
                        and (list[2] is None or i.start >= list[2]) \
                        and (list[3] is None or i.end <= list[3]):
                    new_list.append(i)
            self.refresh(lista=new_list)

    def today(self, widget):
        print "today"
        self.refresh(today=True)

    def reload(self,widget):
        self.refresh()
