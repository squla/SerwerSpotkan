import sys

try:
    import pygtk

    pygtk.require("2.0")
except:
    sys.exit(2)
try:
    import gtk
    import gtk.glade
except:
    sys.exit(1)


class SearchView:
    def __init__(self,wTree):
        self.wTree = wTree
        self.window = self.wTree.get_widget("searchWindow")
        self.treeView = self.wTree.get_widget("treeview2")
        self.treeList = gtk.ListStore(str,str,str)
        self.treeView.set_model(self.treeList)
        self.createColumn()
        if self.window:
            self.window.connect("destroy", gtk.main_quit)

        self.wTree.get_widget("entry2").set_text("Nazwa")
        self.wTree.get_widget("entry1").set_text("1")

    def createColumn(self):
        self.addListColumn("Od", 0)
        self.addListColumn("Do", 1)
        self.addListColumn("Dzien", 2)

    def addListColumn(self, title, columnId):
        column = gtk.TreeViewColumn(title, gtk.CellRendererText(), text=columnId)
        column.set_resizable(True)
        column.set_sort_column_id(columnId)
        self.treeView.append_column(column)

    def getName(self):
        return self.wTree.get_widget("entry2").get_text()

    def getDays(self):
        return int(self.wTree.get_widget("entry1").get_text())

    def hide(self):
        self.window.hide()

    def show(self):
        self.window.show()