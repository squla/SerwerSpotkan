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


class LoginView:
    def __init__(self, wTree):
        self.wTree = wTree
        self.window = self.wTree.get_widget("loginWindow")

        if self.window:
            self.window.connect("destroy", gtk.main_quit)

    def setInfoLabel(self, text):
        """

        :type text: str
        :return:
        """
        infoLabel = self.wTree.get_widget("loginInfoLabel")
        infoLabel.set_text(text)

    def getLogin(self):
        return self.wTree.get_widget("loginEntry").get_text()

    def getPassword(self):
        return self.wTree.get_widget("passwordEntry").get_text()

    def hide(self):
        self.window.hide()

    def show(self):
        self.window.show()
