import time
from SocketIOManager import *
from HC04 import *
from HC04_Sensor import *

# Create websocket client
manager = SocketIOClientManager(server_url)
manager.setup_event_handlers()


def sendSpeed(speed):
    if speed != None:
        manager.sendMessage("setSpeed", speed)

logic_Sensor = HC04(10, 20, 30, sendSpeed)

TRIG_PIN = 23
ECHO_PIN = 24
real_Sensor = HC04_Sensor(TRIG_PIN, ECHO_PIN)
real_Sensor.setupSensor()


while True:

    distance = real_Sensor.get_distance()
    logic_Sensor.process(distance)
    time.sleep(1)
