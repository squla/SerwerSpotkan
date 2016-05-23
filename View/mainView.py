class mainView:
    def __init__(self, wTree):
        self.wTree = wTree
        self.window = self.wTree.get_widget("mainWindow")

    def show(self):
        self.window.show()
