from View.FindUserView import FindUserView
from sqlalchemy.orm import Session
# from Controller.FindController import FindController
from Model.table_def import User


class FindUserController:
    def __init__(self, wTree, view, findView, findController, session):
        """

        :param wTree:
        :type view: FindUserView
        :param findView:
        :type findController: FindController
        :type session: Session
        :return:
        """
        self.view = view
        self.findView = findView
        self.session = session
        self.findController = findController
        self.wTree = wTree
        self.initButton()
        self.list = []

    def initButton(self):
        dic = {
            "on_addFindUserWindowButton": self.add,
            "on_searchFindUserWindowButton": self.search,
            "on_okFindUserWindowButton": self.ok
        }
        self.view.wTree.signal_autoconnect(dic)

    def add(self, widget):
        treeView = self.view.treeView
        selection = treeView.get_selection()
        (model, path) = selection.get_selected_rows()
        tree_iter = model.get_iter(path[0])
        email = model.get_value(tree_iter, 0)
        for i in self.list:
            if i.email == email:
                self.findController.addToList(i)

        print "add"

    def search(self, widget):
        self.view.treeList.clear()
        self.query = self.session.query(User)
        if self.view.getEmail() != "":
            self.query = self.query.filter(User.email == self.view.getEmail())
        if self.view.getName() != "":
            self.query = self.query.filter(User.name == self.view.getName())
        if self.view.getSurname() != "":
            self.query = self.query.filter(User.surname == self.view.getSurname())
        self.list = self.query.all()
        for i in self.list:
            self.view.treeList.append([i.email, i.name, i.surname])
        print "search"

    def ok(self, widget):
        print "Ok"
        self.view.hide()

    def show(self):
        self.view.show()
