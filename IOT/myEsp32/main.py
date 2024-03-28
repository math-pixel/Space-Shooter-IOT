from time import sleep_ms 
from SocketIOManager import *


server_url = 'http://localhost:8000'
manager = SocketIOClientManager(server_url)
manager.setup_event_handlers()
manager.sendMessage("message", {"msg": "Hello from ESP32!"})

while True:
    try:
        print("routine")
        sleep_ms(100)
  
    except KeyboardInterrupt:
        pass