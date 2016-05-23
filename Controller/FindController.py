from Controller.FindUserController import FindUserController
from View.FindUserView import FindUserView
from View.SearchView import SearchView
from Controller.searchController import searchController

from Model.table_def import Activity
class FindController:
    def __init__(self, wTree, view, session, user):
        self.view = view
        self.user = user
        self.wTree = wTree
        self.session = session
        self.initButton()
        self.findUserview = FindUserView(self.wTree)
        self.findUserController = FindUserController(self.wTree, self.findUserview, None, self, session)
        self.list = []
        self.searchView = SearchView(self.wTree)
        self.searchController = searchController(self.wTree, self.searchView, list, session)

    def initButton(self):
        dic = {
            "on_addPendingButton": self.movePendingActivity,
            "on_deletePendingButton": self.removePendingActivity,
            "on_infoPendingButton": self.infoPendingActivity,
            "on_addFindUserButton": self.findUser,
            "on_removeFindUserButton": self.removeUser,
            "on_findFreeTimeButton": self.search,
            "on_clearFindListButton": self.cleanList
        }
        self.wTree.signal_autoconnect(dic)

    def movePendingActivity(self, widget):
        # self.user.move(self.getSelection())
        for i in self.user.waitingActivities_list:
            if i.name == self.getSelection():
                new_activity = Activity(i.name, i.day, i.start, i.end)
                self.user.activities_list.append(new_activity)
                self.session.add(new_activity)
                self.session.delete(i)
                self.session.commit()
                self.session.expire_all()

    print "move"


    def removePendingActivity(self, widget):
        print "remove"
        for i in self.user.waitingActivities_list:
            if i.name == self.getSelection():
                self.session.delete(i)
                self.session.commit()
                self.session.expire_all()
                self.infoPendingActivity(None)


    def infoPendingActivity(self, widget):
        self.session.expire_all()
        self.view.treeListWaitActivity.clear()
        for i in self.user.waitingActivities_list:
            self.view.treeListWaitActivity.append([i.name])
        print "info"


    def getSelection(self):
        treeView = self.view.treeViewWaitActivity
        selection = treeView.get_selection()
        (model, path) = selection.get_selected_rows()
        tree_iter = model.get_iter(path[0])
        return model.get_value(tree_iter, 0)


    def findUser(self, widget):
        self.findUserController.show()
        print "find user"


    def removeUser(self, widget):
        print "remove user"
        treeView = self.view.treeViewUser
        selection = treeView.get_selection()
        (model, path) = selection.get_selected_rows()
        tree_iter = model.get_iter(path[0])
        email = model.get_value(tree_iter, 0)
        for i in self.list:
            if i.email == email:
                self.list.remove(i)
                self.refresh()
                return


    def search(self, widget):
        self.searchController.setuser(self.list)
        self.searchController.show()
        print "find"


    def cleanList(self, wdiget):
        print "clean"
        self.view.treeListUser.clear()
        self.list = []


    def addToList(self, user):
        print user.email
        self.list.append(user)
        self.refresh()


    def refresh(self):
        self.view.treeListUser.clear()
        for i in self.list:
            self.view.treeListUser.append([i.email, i.name, i.surname])
