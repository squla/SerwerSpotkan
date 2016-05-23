import gtk
import gtk.glade


class TodayView:
    def __init__(self, wtree):
        self.wTree = wtree
        assert isinstance(self.wTree, gtk.glade.XML)

        self.treeView = self.wTree.get_widget("todayTreeView")
        assert isinstance(self.treeView, gtk.TreeView)
        print "test"
        self.treeList = gtk.ListStore(str, str, str)
        self.treeView.set_model(self.treeList)
        self.create_column()

    def create_column(self):
        self.add_list_column("nazwa", 0)
        self.add_list_column("od", 1)
        self.add_list_column("do", 2)

    def add_list_column(self, title, columnId):
        column = gtk.TreeViewColumn(title, gtk.CellRendererText(), text=columnId)
        column.set_resizable(True)
        column.set_sort_column_id(columnId)
        self.treeView.append_column(column)
