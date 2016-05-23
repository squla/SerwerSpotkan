from View.TodayView import TodayView
from Model.table_def import User
from datetime import datetime
class TodayController:
    def __init__(self, view, user,session):
        """

        :type view: TodayView
        :type user: User
        """
        self.view = view
        self.user = user
        self.session = session
        self.refresh()

    def refresh(self):
        self.session.expire_all()
        for i in self.user.activities_list:
            if i.day == datetime.now().date():
                self.view.treeList.append(i.getList())
