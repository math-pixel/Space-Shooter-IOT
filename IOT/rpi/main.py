import time
from SocketIOManager import *
from HC04Manager import *
from HC04_Sensor import *
from ButtonManager import *
from ButtonDelegate import *
from HC04Delegate import *

# Create websocket client
server_url = 'http://192.168.107.134:8000'
manager = SocketIOClientManager(server_url)
manager.setup_event_handlers()


# ----------------------------- HC04 sensor logic ---------------------------- #
def sendSpeed(speed):
    manager.sendMessage("setSpeed", speed)
logic_Sensor = HC04Manager(max1=5, max2=9, max3=30, callback=sendSpeed)

# ----------------------------- HC04 Real Sensor ----------------------------- #
TRIG_PIN = 23
ECHO_PIN = 24
real_Sensor = HC04_Sensor(TRIG_PIN, ECHO_PIN)
real_Sensor.setupSensor()

# ---------------------------------- Button ---------------------------------- #
class ActionButton(InterfaceButton):
    def __init__(self):
        pass

    def onClick(self):
        manager.sendMessage("fire", "nothing")

    def onRelease(self):
        print("button release")

delegateActionButton = ActionButton()
button = InputButton(13, delegate=delegateActionButton)

while True:

    distance = real_Sensor.get_distance()
    logic_Sensor.process(distance)
    button.process()
    time.sleep(0.2)
