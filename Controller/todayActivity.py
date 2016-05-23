import gtk
from Model.table_def import User
from sqlalchemy.orm import sessionmaker


class TodayActivity:
    def __init__(self, wTree, user,engine=None):
        self.wTree = wTree
        self.engine = engine
        self.treeView = self.wTree.get_widget("todayTreeView")
        self.treeList = gtk.ListStore(str, str, str)
        self.treeView.set_model(self.treeList)
        self.createColumn()
        self.user = user

    def createColumn(self):
        self.addListColumn("nazwa", 0)
        self.addListColumn("od", 1)
        self.addListColumn("do", 2)

    def addListColumn(self, title, columnId):
        column = gtk.TreeViewColumn(title, gtk.CellRendererText(), text=columnId)
        column.set_resizable(True)
        column.set_sort_column_id(columnId)
        self.treeView.append_column(column)

    def refresh(self):
        for i in self.user.activities_list:
            self.treeList.append(i.getList())
