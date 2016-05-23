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


class FindUserView:
    def __init__(self, wTree):
        self.wTree = wTree
        self.window = self.wTree.get_widget("findUserWindow")
        self.treeView = self.wTree.get_widget("userTreeView")
        self.treeList = gtk.ListStore(str, str, str)
        self.treeView.set_model(self.treeList)
        self.createColumn()
        if self.window:
            self.window.connect("destroy", gtk.main_quit)

    def getEmail(self):
        return self.wTree.get_widget("emailFindUserEntry").get_text()

    def getName(self):
        return self.wTree.get_widget("nameFindUserEntry").get_text()

    def getSurname(self):
        return self.wTree.get_widget("surnameFindUserEntry").get_text()

    def createColumn(self):
        self.addListColumn("email", 0)
        self.addListColumn("imie", 1)
        self.addListColumn("nazwisko", 2)

    def addListColumn(self, title, columnId):
        column = gtk.TreeViewColumn(title, gtk.CellRendererText(), text=columnId)
        column.set_resizable(True)
        column.set_sort_column_id(columnId)
        self.treeView.append_column(column)

    def hide(self):
        self.window.hide()

    def show(self):
        self.window.show()
