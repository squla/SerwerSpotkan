import gtk


class ActivityView:
    def __init__(self, wTree):
        self.wTree = wTree
        self.treeView = self.wTree.get_widget("activityTreeView")
        self.treeList = gtk.ListStore(str, str, str, str)
        self.treeView.set_model(self.treeList)
        self.createColumn()

    def createColumn(self):
        self.addListColumn("nazwa", 0)
        self.addListColumn("dzien", 1)
        self.addListColumn("od", 2)
        self.addListColumn("do", 3)

    def addListColumn(self, title, columnId):
        column = gtk.TreeViewColumn(title, gtk.CellRendererText(), text=columnId)
        column.set_resizable(True)
        column.set_sort_column_id(columnId)
        self.treeView.append_column(column)
