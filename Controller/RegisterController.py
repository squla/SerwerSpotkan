from sqlalchemy.orm import Session
from Model.table_def import User
from View.RegisterView import RegisterView

class RegisterController:
    def __init__(self, wTree, view, session):
        """

        :param wTree:
        :type view: RegisterView
        :type session: Session
        :return:
        """
        self.view = view
        self.wTree = wTree
        self.session = session

        dic = {
            "on_registerOkButton": self.onRegisterOk,
            "on_registerCancelButton": self.onRegisterCancel
        }
        self.wTree.signal_autoconnect(dic)

    def onRegisterOk(self, widget):
        print "RegisterOk"
        if self.view.getPassword() == "":
            self.view.setInfoLabel("Brak Hasla")
            return
        if self.isUnique(self.view.getEmail()):
            print "email ok"
            new_user = User(self.view.getName(),self.view.getSurname(),
                            self.view.getEmail(),self.view.getPassword())
            self.session.add(new_user)
            self.session.commit()
            self.view.hide()
            return
        else:
            self.view.setInfoLabel("Istnieje konto o podanym adresie email")
        print "Error"


    def onRegisterCancel(self, widget):
        print "RegisterCancell"
        self.view.hide()

    def isUnique(self, email):
        return self.session.query(User).filter(User.email == email).count() == 0
