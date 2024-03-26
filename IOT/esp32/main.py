from time import sleep_ms 
import bluetooth
import random
import struct
import time
from wireless_manager import *
from machine import Pin

class BLECallback(CommunicationCallback):

    def __init__(self,bleName="Default"):
        self.bleName = bleName
    
    def connectionCallback(self):
        print("Connected")
    
    def disconnectionCallback(self):
        print("Disconected")
    
    def didReceiveCallback(self,value):
        print(f"Received {value}")
    

class WebsocketCallback(CommunicationCallback):

    def __init__(self):
        pass
    
    def connectionCallback(self):
        print("Connected")
    
    def disconnectionCallback(self):
        print("Disconected")
    
    def didReceiveCallback(self,value):
        print(f"Received {value}")
        
    
wirelessManager = WirelessManager(BLECallback("laMamie"),WebsocketCallback())

print("toto1")
push_button = Pin(13, Pin.In)
print("toto2")
try:
    while True:
        print("toto")
        btn1 = push_button.value()
        print(btn1)
        wirelessManager.process()
        sleep_ms(100)
        
        wirelessManager.sendDataToBLE("Hoho BLE")
        wirelessManager.sendDataToWS("Hoho WS")
            
except KeyboardInterrupt:
    pass
#server.stop()
