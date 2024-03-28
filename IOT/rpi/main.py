import time
from SocketIOManager import *
from HC04 import *
from HC04_Sensor import *
from ButtonManager import *

# Create websocket client
server_url = 'http://localhost:8000'
manager = SocketIOClientManager(server_url)
manager.setup_event_handlers()


# ----------------------------- HC04 sensor logic ---------------------------- #
def sendSpeed(speed):
    if speed != None:
        manager.sendMessage("setSpeed", speed)

logic_Sensor = HC04(10, 20, 30, sendSpeed)

# ----------------------------- HC04 Real Sensor ----------------------------- #
TRIG_PIN = 23
ECHO_PIN = 24
real_Sensor = HC04_Sensor(TRIG_PIN, ECHO_PIN)
real_Sensor.setupSensor()

# ---------------------------------- Button ---------------------------------- #
def buttonPressAction():
    manager.sendMessage("fire")
button = InputButton(13, callbackOnPress=buttonPressAction)

while True:

    distance = real_Sensor.get_distance()
    logic_Sensor.process(distance)
    button.process()
    time.sleep(1)
