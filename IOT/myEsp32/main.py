from time import sleep_ms 
from SocketIOManager import *
from MPU5060_logic import *
from MPU5060_sensor import *
from machine import I2C, Pin

# --------------------------------- Websocket -------------------------------- #
# server_url = 'http://localhost:8000'
# manager = SocketIOClientManager(server_url)
# manager.setup_event_handlers()
# manager.sendMessage("message", {"msg": "Hello from ESP32!"})

# ------------------------------- Logic Sensor ------------------------------- #
threshold = 10
logicSensor = GYRO(threshold)

# -------------------------------- Real Sensor ------------------------------- #
i2c = I2C(scl=Pin(22), sda=Pin(21))     #initializing the I2C method for ESP32
sensorGyro = Gyro_Sensor(i2c)

# -------------------------------- Loop esp32 -------------------------------- #
while True:
    try:
        print("routine")
        sensorGyro.get_values()
        print(sensorGyro.get_values())

        X = 0 # set with gyro Y
        Y = 0 # set with gyro X
        logicSensor.process({"x": X, "y":Y}) #sensorGyro.getGyroData()
        sleep_ms(100)
  
    except KeyboardInterrupt:
        pass