# def find(users, i):
#     lista = []
#     today = datetime.datetime.now().date()
#     for i in 0..i:
#         lista.append(findInday(users, today + datetime.timedelta(days=i)))
#     return lista
#
#
# def findInday(users, day):
#     """
#
#     :type users: list[User]
#     :return:
#     """
#     lista = []
#     for i in users:
#         x = i.getFreeTime(day)
#         l = checkListofTuple(x, users, day)
#         if l:
#             lista.append(l)
#     return lista
#
#
# def checkTupleInList((x, y), userFreeTimes):
#     for i, j in userFreeTimes:
#         if i >= x and j <= y:
#             return True
#     return False
#
#
# def checkTupleInUsers(t, users, day):
#     x, y = t
#     for i in users:
#         if not checkTupleInList((x, y), i.getFreeTime(day)):
#             return False
#     return True
#
#
# def checkListofTuple(x, users, day):
#     for i in x:
#         if checkTupleInUsers(i, users, day):
#             return i
#
#     return None


def find2(listTuples):
    lista = []
    for i in listTuples:  # iterujemy po ltuple
        for j in i:  # iterujemy po kazdej krotce
            lista.append(j)
    wynik = []
    for x, y in lista:
        wynik.append(find((x, y), lista))

    return list(set(wynik))


def find((x, y), tuples):
    for k, l in tuples:
        if x <= k <= y:
            x = k
        if y >= l >= x:
            y = l
    return x, y


import datetime

if __name__ == '__main__':
    ltuple1 = [(6, 7), (14, 24)]
    ltuple2 = [(6.30, 7), (14.45, 18), (23, 24)]
    ltuple3 = [(5.30, 6.50), (17, 24)]
    dtuple1 = [(datetime.time(6), datetime.time(7)), (datetime.time(14), datetime.time(23))]
    dtuple2 = [(datetime.time(6, 30), datetime.time(7)), (datetime.time(14, 45), datetime.time(18)),
               (datetime.time(22,0,0), datetime.time(23,59,59))]
    dtuple3 = [(datetime.time(5, 30), datetime.time(6, 50)), (datetime.time(17), datetime.time(23,59,59))]
    tuples = [ltuple1, ltuple2, ltuple3]
    dtuples = [dtuple1, dtuple2, dtuple3]
    l = find2(tuples)
    z = find2(dtuples)
    for i in z:
        print str(i)
