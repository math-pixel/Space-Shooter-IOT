import urllib
from SequenceTesteur import TestableClass
from Display import *

class WIFI(TestableClass):

    def __init__(self) -> None:
        pass

    def testSensor(self):
        try:
            url = "https://www.google.com"
            urllib.urlopen(url)
            status = "Connected"
            return DISPLAY.SUCCESS
        except:
            status = "Not connected"
            return DISPLAY.ERROR_SENSOR

    

