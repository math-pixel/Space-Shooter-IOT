
class HC04():

    def __init__(self, max1, max2, max3, callback) -> None:
        self.state = HC04_State_Range_Unknown(self)
        self.max1 = max1
        self.max2 = max2
        self.max3 = max3
        self.callback = callback

    def process(self, valueSensor):
        if valueSensor <= self.max1:
            self.updateState(HC04_State_Range_1(self)) 
        elif valueSensor > self.max1 and valueSensor <= self.max2:
            self.updateState(HC04_State_Range_2(self)) 
        elif valueSensor > self.max2 and valueSensor <= self.max3:
            self.updateState(HC04_State_Range_3(self)) 
        else:
           self.updateState(HC04_State_Range_Unknown(self)) 

    def actionRange1(self):
        self.callback(2)
    def actionRange2(self):
        self.callback(5)
    def actionRange3(self):
        self.callback(12)
    def actionRangeUnknown(self):
        # self.callback(0)
        print("unknow")

    def updateState(self, state):
        self.state = state

# --------------------------------- interface -------------------------------- #
class HC04_State():

    def actionRange1(self):
        pass
    def actionRange2(self):
        pass
    def actionRange3(self):
        pass
    def actionRangeUnknown(self):
        pass

# ----------------------------------- State ---------------------------------- #
class HC04_State_Range_1(HC04_State):

    def __init__(self, HC04) -> None:
        self.sensor = HC04
        print("state 1")
        self.sensor.actionRange1()


    def actionRange1(self):
        pass
    def actionRange2(self):
        self.sensor.updateState(HC04_State_Range_2(self.sensor))
    def actionRange3(self):
        self.sensor.updateState(HC04_State_Range_3(self.sensor))
    def actionRangeUnknown(self):
        self.sensor.updateState(HC04_State_Range_Unknown(self.sensor))



class HC04_State_Range_2(HC04_State):

    def __init__(self, HC04) -> None:
        self.sensor = HC04
        print("state 2")
        self.sensor.actionRange2()


    def actionRange1(self):
        self.sensor.updateState(HC04_State_Range_1(self.sensor))
    def actionRange2(self):
        pass
    def actionRange3(self):
        self.sensor.updateState(HC04_State_Range_3(self.sensor))
    def actionRangeUnknown(self):
        self.sensor.updateState(HC04_State_Range_Unknown(self.sensor))


class HC04_State_Range_3(HC04_State):

    def __init__(self, HC04) -> None:
        self.sensor = HC04
        print("state 3")
        self.sensor.actionRange3()



    def actionRange1(self):
        self.sensor.updateState(HC04_State_Range_1(self.sensor))
    def actionRange2(self):
        self.sensor.updateState(HC04_State_Range_2(self.sensor))
    def actionRange3(self):
        pass
    def actionRangeUnknown(self):
        self.sensor.updateState(HC04_State_Range_Unknown(self.sensor))

class HC04_State_Range_Unknown(HC04_State):

    def __init__(self, HC04) -> None:
        self.sensor = HC04
        print("state unknow")
        self.sensor.actionRangeUnknown()


    def actionRange1(self):
        self.sensor.updateState(HC04_State_Range_1(self.sensor))
    def actionRange2(self):
        self.sensor.updateState(HC04_State_Range_2(self.sensor))
    def actionRange3(self):
        self.sensor.updateState(HC04_State_Range_3(self.sensor))
    def actionRangeUnknown(self):
        pass


# def printSpeed(speed):
#     print(speed)

# mySensor = HC04(10, 20, 30, printSpeed)

# mySensor.process(5)
# mySensor.process(15)
# mySensor.process(25)

