from View.LoginView import LoginView
from sqlalchemy.orm import Session
from Model.table_def import User
from Controller.mainController import mainController


class LoginController:
    def __init__(self, wTree, view, mainView, registerView, session):
        """

        :type view: LoginView
        :type session: Session
        """
        self.view = view
        self.wTree = wTree
        self.mainView = mainView
        self.registerView = registerView
        self.user = None
        self.session = session
        dic = {"on_registerButton": self.onRegister,
               "on_loginButton": self.onLogin}
        self.view.wTree.signal_autoconnect(dic)

    def onRegister(self, widget):
        print "click Register Button"
        self.registerView.show()
        self.view.setInfoLabel("Register")

    def onLogin(self, widget):
        print "click Login Button"
        user = self.getLogin()
        if user:
            if self.checkPassword(user, self.view.getPassword()):
                self.view.setInfoLabel("Sukces")
                mainController(self.wTree, user, self.session)
                self.user = user
                self.successLogin()

            else:
                self.view.setInfoLabel("Bledne Haslo")
        else:
            self.view.setInfoLabel("Brak uzytkownika o takim email")

    def getLogin(self):
        email = self.view.getLogin()
        print("Login: " + email)
        return self.session.query(User).filter(User.email == email).first()

    def checkPassword(self, user, password):
        """

        :type user: User
        :type password: str
        :return:
        """
        return user.checkPassword(password)

    def successLogin(self):
        self.view.hide()
        self.mainView.show()

    def getUser(self):
        return self.user
