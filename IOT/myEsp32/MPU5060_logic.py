class MPU5060GYROLogic():

    def __init__(self, threshold , valueIdleX = 0, valueIdleY = 0) -> None:
        self.threshold = threshold
        self.valueIdleX = valueIdleX
        self.valueIdleY = valueIdleY

    def process(self, valueGyro):
        valueX = "idle"
        valueY = "idle"

        # state X
        if valueGyro["AcX"] < self.valueIdleX - self.threshold:
            valueX = "right"
        elif valueGyro["AcX"] > self.valueIdleX + self.threshold:
            valueX = "left"
        else:
            valueX = "idle"

        # state Y
        if valueGyro["AcY"] < self.valueIdleY - self.threshold:
            valueY = "up"
        elif valueGyro["AcY"] > self.valueIdleY + self.threshold:
            valueY = "down"
        else:
            valueY = "idle"

        return { "x": valueX, "y":valueY }