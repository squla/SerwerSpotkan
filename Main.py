import sys
from Controller.todayActivity import TodayActivity
from Controller.activityController import ActivityController
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from Model.table_def import User
from View.LoginView import LoginView
from Controller.mainController import mainController
from View.mainView import mainView
from Controller.LoginController import LoginController
from Controller.RegisterController import RegisterController
from View.RegisterView import RegisterView

try:
    import pygtk

    pygtk.require("2.0")
except:
    pass
try:
    import gtk
    import gtk.glade
except:
    sys.exit(1)

engine = create_engine('sqlite:///spotkaniaTest.db', echo=False)


class Ctest:
    def __init__(self):
        self.gladefile = "serwerspotkan.glade"
        self.wTree = gtk.glade.XML(self.gladefile)
        self.window = self.wTree.get_widget("window1")
        Session = sessionmaker(bind=engine)
        session = Session()
        self.loginView = LoginView(self.wTree)
        self.registerView = RegisterView(self.wTree, self.loginView)
        self.mainView = mainView(self.wTree)
        RegisterController(self.wTree, self.registerView, session)
        LoginController(self.wTree, self.loginView, self.mainView, self.registerView, session)

        # if (self.window):
        #     self.window.connect("destroy", gtk.main_quit)
        #     self.window.connect("")

        # dic = {"on_loginWindow_destroy": gtk.main_quit,
        #        "on_mainWindow_destroy": gtk.main_quit}
        #
        # self.wTree.signal_autoconnect(dic)
        # Session = sessionmaker(bind=engine)
        # session = Session()
        # user = session.query(User).filter(User.name == "Test").first()
        # x = TodayActivity(self.wTree, user)
        # y = ActivityController(self.wTree, user)

        # def On_Button(self,widget):
        #     self.window.hide()
        #     self.window2 = self.wTree.get_widget("window2")
        #     self.window2.show()


if __name__ == '__main__':
    wine = Ctest()
    gtk.main()
    exit()
