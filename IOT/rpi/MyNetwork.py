import urllib
from SequenceTesteur import TestableClass
from Display import *

class WIFI(TestableClass):

    def __init__(self) -> None:
        pass

    def testSensor(self):
        status = DISPLAY.ERROR_SENSOR
        try:
            url = "https://www.google.com"
            urllib.urlopen(url)
            status = DISPLAY.SUCCESS
             
        except:
            pass
        
        return status

