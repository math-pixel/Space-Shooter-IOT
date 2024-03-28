from time import sleep_ms 
from SocketIOManager import *
from MPU5060_logic import *
from MPU5060_sensor import *

server_url = 'http://localhost:8000'
manager = SocketIOClientManager(server_url)
manager.setup_event_handlers()
manager.sendMessage("message", {"msg": "Hello from ESP32!"})

threshold = 10
logicSensor = GYRO(threshold)

sensorGyro = Gyro_Sensor()

while True:
    try:
        print("routine")
        logicSensor.process(sensorGyro.getGyroData())
        sleep_ms(100)
  
    except KeyboardInterrupt:
        pass