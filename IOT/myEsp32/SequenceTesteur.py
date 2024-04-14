import time
from Display import *

# Interface For sensor testable
class TestableClass:

    def __init__(self) -> None:
        pass

    def testSensor(self):
        pass


class Testeur:

    intervalTimeIntoPhase = 2

    def __init__(self) -> None:
        pass

    @staticmethod
    def TestSensors(arraySensor):
        
        indexOfTest = 1
        for sensor in arraySensor:

            Displayer.displayErrorCode(DISPLAY.PHASE_X, indexOfTest)
            indexOfTest += 1

            resultCode = sensor.testSensor()
            Displayer.displayErrorCode(resultCode)
            time.sleep(Testeur.intervalTimeIntoPhase)

# allSensors = [*list of Sensor*]
# Testeur.TestSensors(allSensors)