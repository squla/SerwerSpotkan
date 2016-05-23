import datetime
import gtk
import gtk.glade
from time import mktime
import time
from Model.table_def import Activity


class AddActivityDialog:
    def __init__(self, wTree, name="", day=datetime.datetime.now().date(),
                 start=datetime.datetime.now().time(),
                 end=datetime.datetime.now().time()):
        # self.wTree = wTree
        self.activity = Activity(name, day, start, end)
        self.gladefile = "serwerspotkan.glade"
        self.wTree = gtk.glade.XML(self.gladefile, "addDialog")

    def run(self):
        self.dlg = self.wTree.get_widget("addDialog")

        nameEnt = self.wTree.get_widget("nameEntry")
        nameEnt.set_text("Nazwa")

        dayEnt = self.wTree.get_widget("dayEntry")
        dayEnt.set_text(self.activity.day.strftime("%Y-%m-%d"))

        startEnt = self.wTree.get_widget("startEntry")
        startEnt.set_text(self.activity.start.strftime("%H:%M"))

        stopEnt = self.wTree.get_widget("endEntry")
        stopEnt.set_text(self.activity.start.strftime("%H:%M"))

        result = self.dlg.run()

        name = nameEnt.get_text()
        day = dayEnt.get_text()
        start = startEnt.get_text()
        stop = stopEnt.get_text()

        self.activity.name = name
        startTime = datetime.datetime.strptime(start, "%H:%M").time()
        self.activity.start = startTime

        stopTime = datetime.datetime.strptime(stop, "%H:%M").time()
        self.activity.end = stopTime

        dayTime = datetime.datetime.strptime(day, "%Y-%m-%d").date()
        self.activity.day = dayTime
        # print self.activity.getList(True)

        self.dlg.destroy()
        return result, self.activity


class RemoveActivityDialog:
    def __init__(self, wTree):
        self.treeView = wTree.get_widget("activityTreeView")
        # self.treeView = self.view.treeView
        self.selection = self.treeView.get_selection()

    def getValue(self):
        (model, path) = self.selection.get_selected_rows()
        tree_iter = model.get_iter(path[0])
        return (model.get_value(tree_iter, 0), model.get_value(tree_iter, 1)
                , model.get_value(tree_iter, 2), model.get_value(tree_iter, 3))

    def run(self):
        return self.getValue()


class EditActivityDialog:
    def __init__(self, activity):
        self.gladefile = "serwerspotkan.glade"
        self.wTree = gtk.glade.XML(self.gladefile, "editDialog")
        self.activity = activity

    def run(self):
        self.dlg = self.wTree.get_widget("editDialog")

        nameEnt = self.wTree.get_widget("nameEntry1")
        nameEnt.set_text(self.activity.name)

        dayEnt = self.wTree.get_widget("dayEntry1")
        dayEnt.set_text(self.activity.day.strftime("%Y-%m-%d"))

        startEnt = self.wTree.get_widget("startEntry1")
        startEnt.set_text(self.activity.start.strftime("%H:%M"))

        stopEnt = self.wTree.get_widget("endEntry1")
        stopEnt.set_text(self.activity.start.strftime("%H:%M"))

        result = self.dlg.run()

        name = nameEnt.get_text()
        day = dayEnt.get_text()
        start = startEnt.get_text()
        stop = stopEnt.get_text()

        self.activity.name = name
        startTime = datetime.datetime.strptime(start, "%H:%M").time()
        self.activity.start = startTime

        stopTime = datetime.datetime.strptime(stop, "%H:%M").time()
        self.activity.end = stopTime

        dayTime = datetime.datetime.strptime(day, "%Y-%m-%d").date()
        self.activity.day = dayTime
        # print self.activity.getList(True)

        self.dlg.destroy()
        return result, self.activity


class FindActivityDialog:
    def __init__(self):
        # self.wTree = wTree
        self.gladefile = "serwerspotkan.glade"
        self.wTree = gtk.glade.XML(self.gladefile, "findDialog")
        self.dlg = self.wTree.get_widget("findDialog")

    def run(self):

        nameEnt = self.wTree.get_widget("nameEntry2")
        dayEnt = self.wTree.get_widget("dayEntry2")
        startEnt = self.wTree.get_widget("startEntry2")
        stopEnt = self.wTree.get_widget("endEntry2")

        result = self.dlg.run()

        name = nameEnt.get_text()
        day = dayEnt.get_text()
        start = startEnt.get_text()
        stop = stopEnt.get_text()

        if name == "":
            name = None

        if start != "":
            startTime = datetime.datetime.strptime(start, "%H:%M").time()
        else:
            startTime = None
        if stop != "":
            stopTime = datetime.datetime.strptime(stop, "%H:%M").time()
        else:
            stopTime = None
        if day != "":
            dayTime = datetime.datetime.strptime(day, "%Y-%m-%d").date()
        else:
            dayTime = None

        self.dlg.destroy()
        return result, [name, dayTime, startTime, stopTime]
