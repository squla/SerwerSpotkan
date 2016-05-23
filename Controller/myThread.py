import threading
import time


class myThread(threading.Thread):
    def __init__(self, controllers):
        threading.Thread.__init__(self)
        self.controllers = controllers


    def run(self):

        #time.sleep(20)
        for i in self.controllers:
            i.refresh()
