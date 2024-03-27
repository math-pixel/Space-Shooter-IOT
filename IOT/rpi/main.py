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

i =  0
while True:
    logic_Sensor.process(i)
    time.sleep(1)
    i += 1
