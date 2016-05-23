from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import DateTime, Time
from sqlalchemy.orm import relationship, backref, sessionmaker
import hashlib
import datetime

engine = create_engine('sqlite:///../spotkaniaTest.db', echo=False)
Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    hashPassword = Column(String)
    # activities_list = relationship("Activity")
    activities_list = relationship("Activity", foreign_keys="Activity.user_id")
    waitingActivities_list = relationship("Activity", foreign_keys="Activity.user2_id")

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.hashPassword = hashlib.md5(password).hexdigest()
        # print type(self.activities_list)

    def checkPassword(self, password):
        return self.hashPassword == hashlib.md5(password).hexdigest()

    def move(self, name):
        for i in self.waitingActivities_list:
            if i.name == name:
                Session = sessionmaker(bind=engine)
                session = Session()
                new_activity = Activity(i.name, i.day, i.start, i.end)
                self.activities_list.append(new_activity)
                session.add(new_activity)
                session.delete(i)
                session.commit()
                session.expire_all()

    def getFreeTime(self, day):
        activities = []
        for i in self.activities_list:
            if i.day == day:
                activities.append(i)

        freeTime = []
        if (activities == []):
            freeTime.append((datetime.time(0, 0, 0), datetime.time(23, 59, 59)))

        x = datetime.time()
        for j in activities:
            p = (x, j.start)
            if not p[0] == p[1]:
                freeTime.append(p)
            x = j.end
        if x <= datetime.time(23, 59, 59):
            freeTime.append((x, datetime.time(23, 59, 59)))

        return freeTime


class Activity(Base):
    __tablename__ = "activity"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    day = Column(Date)
    start = Column(Time)
    end = Column(Time)
    # user_id = Column(Integer, ForeignKey("user.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    user2_id = Column(Integer, ForeignKey("user.id"))

    def __init__(self, name, day, start, end):
        self.name = name
        self.start = start
        self.end = end
        self.day = day

    def getList(self, withDay=False):
        if withDay: return [str(self.name), str(self.day), str(self.start), str(self.end)]
        return [str(self.name), str(self.start), str(self.end)]


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
print
new_user = User("Test", "Test1", "test@com.pl", "test")
new_activity1 = Activity("testActivity1", datetime.date(2016, 1, 1), datetime.time(0), datetime.time(6))
new_activity2 = Activity("testActivity2", datetime.date(2016, 1, 1), datetime.time(7), datetime.time(14))
new_user.activities_list.append(new_activity1)
new_user.activities_list.append(new_activity2)

session.add(new_user)
session.add(new_activity2)
session.add(new_activity1)
session.commit()

res = session.query(User).filter(User.name == "Test").first()
for i in res.activities_list:
    print str(i.start) + " " + str(i.end) + " " + str(i.day)

for k in res.getFreeTime(datetime.date(2016, 1, 1)):
    print str(k[0]) + "  // " + str(k[1])
