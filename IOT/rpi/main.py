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
class ActionDelegateHC04(InterfaceHC04Delegate):
    def __init__(self) -> None:
        pass

    def actionRange1(self):
        manager.sendMessage("setSpeed", 2)

    def actionRange2(self):
        manager.sendMessage("setSpeed", 6)

    def actionRange3(self):
        manager.sendMessage("setSpeed", 10)
        
    def errorRange(self):
        print("error")

actionHC04 = ActionDelegateHC04()
logic_Sensor = HC04Manager(max1=10, max2=20, max3=30, delegate=actionHC04)

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

delegateActionButton = ActionButton()
button = InputButton(13, delegate=delegateActionButton)

while True:

    distance = real_Sensor.get_distance()
    logic_Sensor.process(distance)
    button.process()
    time.sleep(1)
