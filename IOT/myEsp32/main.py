from time import sleep_ms 
from MPU5060_logic import *
from MPU5060_sensor import *
from machine import I2C, Pin

import requests

server_url = "192.168.107.134:8000/dataGyro"
#server_url = "http://192.168.107.134:8000"

mylastX = ""
mylastY = ""
def sendMouvementHTTP(mouvement):
    global mylastX
    global mylastY
    print("mouv" , mouvement)
    print("last" , mylastX, mylastY)
    if mouvement["x"] != mylastX or mouvement["y"] != mylastY:
        mylastX = mouvement["x"]
        mylastY = mouvement["y"]
        myrequest = url = "http://{}/?x={}&y={}".format(server_url, mylastX, mylastY)
        print("NEW request :", myrequest)
        rep = requests.get(myrequest)
        
        print("Response Status Code:", rep.status_code)
        print("Response Content:", rep.text)
        rep.close()
    else:
        pass #print("same than last value")

# --------------------------------- Websocket -------------------------------- #
# manager = SocketIOClientManager(server_url)
# manager.setup_event_handlers()
# manager.sendMessage("message", {"msg": "Hello from ESP32!"})

# ------------------------------- Logic Sensor ------------------------------- #
threshold = 10000
logicSensor = GYRO(threshold)

# -------------------------------- Real Sensor ------------------------------- #
i2c = I2C(scl=Pin(22), sda=Pin(21))     #initializing the I2C method for ESP32
sensorGyro = Gyro_Sensor(i2c)

# -------------------------------- Loop esp32 -------------------------------- #
while True:
    try:
        print("routine")
        valueSensor = sensorGyro.get_values()
        #print("X : ", sensorGyro.get_values()["AcX"], " ", "Y : ", sensorGyro.get_values()["AcY"])

        X = valueSensor["AcX"] 
        Y = valueSensor["AcY"] 
        mouvement = logicSensor.process({"x": X, "y":Y}) #sensorGyro.getGyroData()
        sendMouvementHTTP(mouvement)
        sleep_ms(100)
  
    except KeyboardInterrupt:
        pass