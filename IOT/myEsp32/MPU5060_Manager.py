
class MPU6050GyroManager():

    def __init__(self, sensor, logicSensor, delegateSensor) -> None:
        self.sensor = sensor
        self.logicSensor = logicSensor
        self.delegateSensor = delegateSensor

    def process(self):
        valueSensor = self.sensor.get_values()
        stateSensor = self.logicSensor.process(valueSensor)

        try:

            if stateSensor["x"] == "idle":
                self.delegateSensor.onIdleX()
            elif stateSensor["x"] == "left":
                self.delegateSensor.onLeft()
            elif stateSensor["x"] == "right":
                self.delegateSensor.onRight()   
        except:
            self.delegateSensor.errorX()
            
        try:

            if stateSensor["y"] == "idle":
                self.delegateSensor.onIdleY()
            elif stateSensor["y"] == "down":
                self.delegateSensor.onDown()
            elif stateSensor["y"] == "up":
                self.delegateSensor.onUp()
        except:
            self.delegateSensor.errorY()

        try:
            
            if stateSensor["z"] == "idle":
                self.delegateSensor.onIdleZ()
            elif stateSensor["z"] == "low":
                self.delegateSensor.onDownZ()
            elif stateSensor["z"] == "hight":
                self.delegateSensor.onUpZ()
        except:
            self.delegateSensor.errorZ()

