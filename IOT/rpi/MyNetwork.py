import subprocess
from SequenceTesteur import TestableClass
from Display import *

class WIFI(TestableClass):

    def __init__(self) -> None:
        pass

    def testSensor(self):
        resultat = subprocess.run(['iwgetid'], capture_output=True, text=True)
        if resultat.stdout.strip():
            return DISPLAY.SUCCESS
        else:
            return DISPLAY.ERROR_SENSOR

