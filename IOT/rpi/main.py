import time
from SocketIOManager import *
from HC04 import *


# Create websocket client
manager = SocketIOClientManager(server_url)
manager.setup_event_handlers()


def sendSpeed(speed):
    manager.sendMessage("setSpeed", speed)

logic_Sensor = HC04(10, 20, 30, sendSpeed)


while True:
    logic_Sensor.process(5)
