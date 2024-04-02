# Interface Delegate
class DelegateGyroSensorInterface():

    def __init__(self) -> None:
        pass

    def onIdleX(self):
        pass
    def onLeft(self):
        pass
    def onRight(self):
        pass
    def errorX(self):
        pass

    def onIdleY(self):
        pass
    def onDown(self):
        pass
    def onUp(self):
        pass
    def errorY(self):
        pass

    def onIdleZ(self):
        pass
    def onDownZ(self):
        pass
    def onUpZ(self):
        pass
    def errorZ(self):
        pass


