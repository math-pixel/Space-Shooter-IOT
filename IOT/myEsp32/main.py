from time import sleep_ms 
from MPU5060_logic import *
from MPU5060_sensor import *
from MPU5060_Manager import *
from DelegateGyroSensor import *
from machine import I2C, Pin

import requests

server_url = "192.168.107.134:8000/dataGyro"
#server_url = "http://192.168.107.134:8000"

currentGyroX = "idle"
currentGyroY = "idle"
mylastX = ""
mylastY = ""
def sendMouvementHTTP():
    global mylastX
    global mylastY
    if currentGyroX != mylastX or currentGyroY != mylastY:
        mylastX = currentGyroX
        mylastY = currentGyroY
        url = "http://{}/?x={}&y={}".format(server_url, mylastX, mylastY)
        print("NEW request :", url)
        rep = requests.get(url)
        
        print("Response Status Code:", rep.status_code)
        print("Response Content:", rep.text)
        rep.close()
    else:
        pass #print("same than last value")

# --------------------------------- Websocket -------------------------------- #
# manager = SocketIOClientManager(server_url)
# manager.setup_event_handlers()
# manager.sendMessage("message", {"msg": "Hello from ESP32!"})

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
        global currentGyroX
        currentGyroX = "idle"
        sendMouvementHTTP()

    def onLeft(self):
        global currentGyroX
        currentGyroX = "left"
        sendMouvementHTTP()

    def onRight(self):
        global currentGyroX
        currentGyroX = "right"
        sendMouvementHTTP()
    
    def onIdleY(self):
        global currentGyroY
        currentGyroY = "idle"
        sendMouvementHTTP()

    def onUp(self):
        global currentGyroY
        currentGyroY = "up"
        sendMouvementHTTP()

    def onDown(self):
        global currentGyroY
        currentGyroY = "down"
        sendMouvementHTTP()

actionDelegation = actionGyroSensor()
    
# ------------------------------ managerMPU5060 ------------------------------ #
managerMPU5060 = MPU6050GyroManager(sensorGyro, logicSensor, actionDelegation)


# -------------------------------- Loop esp32 -------------------------------- #
while True:
    try:
        managerMPU5060.process()
        sleep_ms(100)
  
    except KeyboardInterrupt:
        pass