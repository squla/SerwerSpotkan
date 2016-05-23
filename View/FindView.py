import gtk


class FindView:
    def __init__(self, wTree):
        self.wTree = wTree
        self.treeViewUser = self.wTree.get_widget("treeview1")
        self.treeListUser = gtk.ListStore(str, str, str)
        self.treeViewUser.set_model(self.treeListUser)

        self.treeViewWaitActivity = self.wTree.get_widget("treeview11")
        self.treeListWaitActivity = gtk.ListStore(str)
        self.treeViewWaitActivity.set_model(self.treeListWaitActivity)
        self.createColumn()

    def createColumn(self):
        self.addListColumn("email", 0, self.treeViewUser)
        self.addListColumn("imie", 1, self.treeViewUser)
        self.addListColumn("nazwisko", 2, self.treeViewUser)
        self.addListColumn("zadanie", 0, self.treeViewWaitActivity)

    def addListColumn(self, title, columnId, tree):
        column = gtk.TreeViewColumn(title, gtk.CellRendererText(), text=columnId)
        column.set_resizable(True)
        column.set_sort_column_id(columnId)
        tree.append_column(column)
