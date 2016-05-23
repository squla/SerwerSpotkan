from sqlalchemy import create_engine

engine = create_engine('sqlite:///../spotkania.db', echo=False)


class LogicController():
    def __init__(self, users):
        self.date
        self.users

    @staticmethod
    def is_user_have_time(user, time):
        for i in user.getFreeTime():
            if time[0] >= i[0] and time[1] <= i[1]:
                return True
        return False

    def check_users(self, time):
        for i in self.users:
            if not self.is_user_have_time(i, time):
                return False
        return True

    def find_times(self, date):
        self.date = date
        for i in self.users:
            for j in i.getFreeTime():
                pass
