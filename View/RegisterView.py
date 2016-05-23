import sys
from View.LoginView import LoginView
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


class RegisterView:
    def __init__(self, wTree, loginView):
        self.wTree = wTree
        self.loginView = loginView
        self.window = self.wTree.get_widget("registerWindow")
        if self.window:
            self.window.connect("destroy", gtk.main_quit)

    def setInfoLabel(self, text):
        infoLabel = self.wTree.get_widget("infoRegisterLabel")
        infoLabel.set_text(text)

    def getEmail(self):
        return self.wTree.get_widget("emailRegisterEntry").get_text()

    def getName(self):
        return self.wTree.get_widget("nameRegisterEntry").get_text()

    def getSurname(self):
        return self.wTree.get_widget("surnameRegisterEntry").get_text()

    def getPassword(self):
        return self.wTree.get_widget("passwordRegisterEntry").get_text()

    def hide(self):
        print "est"
        self.loginView.show()
        self.window.hide()


    def show(self):
        self.loginView.hide()
        self.window.show_all()
