from time import sleep_ms 
from MPU5060_logic import *
from MPU5060_sensor import *
from MPU5060_Manager import *
from DelegateGyroSensor import *
from machine import I2C, Pin
from SequenceTesteur import *
from MyNetwork import *

import requests
server_url = "192.168.107.134:8000/"
directory = "dataGyro"
#server_url = "http://192.168.107.134:8000" 

class SenderManager(TestableClass):

    def __init__(self, server_url, directory) -> None:
        self.x = ""
        self.y = ""
        self.lastX = ""
        self.lastY = ""
        self.server_url = server_url
        self.directory = directory

    def updateAxe(self, axe, newValue):
        if axe == "x":
            self.x = newValue
        else:
            self.y = newValue
    
    def testSensor(self):
        url = "http://{}/".format(self.server_url)
        rep = requests.get(url)
        if rep.status_code == 200:
            return DISPLAY.SUCCESS
        else:
            return DISPLAY.ERROR_SENSOR
        rep.close()

    def sendMouvement(self):
        if self.lastX != self.x or self.lastY != self.y:
            self.lastX = self.x
            self.lastY = self.y
            url = "http://{}/?x={}&y={}".format(self.server_url + self.directory, self.x, self.y)
            print("NEW request :", url)
            rep = requests.get(url)
            
            print("Response Status Code:", rep.status_code)
            print("Response Content:", rep.text)
            rep.close()


# --------------------------------- Websocket -------------------------------- #
# manager = SocketIOClientManager(server_url)
# manager.setup_event_handlers()
# manager.sendMessage("message", {"msg": "Hello from ESP32!"})
senderInformation = SenderManager(server_url, directory)
# ---------------------------------------------------------------------------- #
#                                  Gyro Sensor                                 #
# ---------------------------------------------------------------------------- #

# -------------------------------- Real Sensor ------------------------------- #
i2c = I2C(scl=Pin(22), sda=Pin(21))     #initializing the I2C method for ESP32
sensorGyro = Gyro_Sensor(i2c)

# ------------------------------- Logic Sensor ------------------------------- #
threshold = 10000
logicSensor = MPU5060GYROLogic(threshold)

# ----------------------- Delegate action of the sensor ---------------------- #
class actionGyroSensor(DelegateGyroSensorInterface):

    def __init__(self) -> None:
        super().__init__()

    def onIdleX(self):
        senderInformation.updateAxe("x", "idle")
        senderInformation.sendMouvement()

    def onLeft(self):
        senderInformation.updateAxe("x", "left")
        senderInformation.sendMouvement()

    def onRight(self):
        senderInformation.updateAxe("x", "right")
        senderInformation.sendMouvement()
    
    def onIdleY(self):
        senderInformation.updateAxe("y", "idle")
        senderInformation.sendMouvement()

    def onUp(self):
        senderInformation.updateAxe("y", "up")
        senderInformation.sendMouvement()

    def onDown(self):
        senderInformation.updateAxe("y", "down")
        senderInformation.sendMouvement()

actionDelegation = actionGyroSensor()

# ------------------------------ managerMPU5060 ------------------------------ #
managerMPU5060 = MPU6050GyroManager(sensorGyro, logicSensor, actionDelegation)

# ------------------------------- Testing Phase ------------------------------ #
wifiTesteur = WIFI()
allSensors = [wifiTesteur, senderInformation, sensorGyro]
Testeur.TestSensors(allSensors)

# -------------------------------- Loop esp32 -------------------------------- #
while True:
    try:
        managerMPU5060.process()
        sleep_ms(100)
  
    except KeyboardInterrupt:
        pass