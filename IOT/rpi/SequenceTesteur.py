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
        
        for sensor in arraySensor:

            index = arraySensor.index(sensor)

            # display phase test X
            Displayer.displayErrorCode(DISPLAY.PHASE_X, index, 0.5)
            time.sleep(Testeur.intervalTimeIntoPhase)

            resultCode = sensor.testSensor()
            Displayer.displayErrorCode(resultCode)
            time.sleep(Testeur.intervalTimeIntoPhase)

# allSensors = [*list of Sensor*]
# Testeur.TestSensors(allSensors)