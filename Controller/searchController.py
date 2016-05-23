import datetime
from Model.table_def import Activity


class searchController:
    def __init__(self, wTree, view, users, session):
        self.wTree = wTree
        self.view = view
        self.users = users
        self.initButton()
        self.dateList = []
        self.session = session

    def setuser(self, users):
        self.users = users

    def initButton(self):
        dic = {
            "on_button1": self.search,
            "on_button2": self.add,
            "on_button3": self.cancel
        }
        self.view.wTree.signal_autoconnect(dic)

    def search(self, widget):
        days = self.view.getDays()
        self.view.treeList.clear()
        for i in range(days):
            usersFreeTimeList = []
            today = datetime.datetime.now().date()
            today += datetime.timedelta(days=i)
            for j in self.users:
                usersFreeTimeList.append(j.getFreeTime(today))
            self.load(self.find2(usersFreeTimeList), today)
        print "search"

    def add(self, widget):
        od, do, dzien = self.getSelection()
        self.activityMailer(self.view.getName(), dzien, od, do)
        self.view.hide()
        print "add"

    def getSelection(self):
        treeView = self.view.treeView
        selection = treeView.get_selection()
        (model, path) = selection.get_selected_rows()
        tree_iter = model.get_iter(path[0])
        i = model.get_value(tree_iter, 0)
        j = model.get_value(tree_iter, 1)
        day = model.get_value(tree_iter, 2)
        for x, y, z in self.dateList:
            if str(x) == i and str(y) == j and str(z) == day:
                return x, y, z

    def cancel(self, widget):
        self.view.hide()
        print "cancel"

    def show(self):
        self.view.show()

    def load(self, lista, dzien):
        # self.view.treeList.clear()
        self.dateList = []
        for i, j in lista:
            self.view.treeList.append([str(i), str(j), str(dzien)])
            self.dateList.append((i, j, dzien))

    def find2(self, mylistTuples):
        lista = []
        for i in mylistTuples:  # iterujemy po ltuple
            for j in i:  # iterujemy po kazdej krotce
                lista.append(j)
        wynik = []
        for x, y in lista:
            wynik.append(self.find((x, y), lista))

        return list(set(wynik))

    def find(self, (x, y), tuples):
        for k, l in tuples:
            if x <= k <= y:
                x = k
            if y >= l >= x:
                y = l
        return x, y

    def activityMailer(self, name, dzien, od, do):
        for i in self.users:
            activity = Activity(name, dzien, od, do)
            i.waitingActivities_list.append(activity)
            self.session.add(activity)
            self.session.commit()
