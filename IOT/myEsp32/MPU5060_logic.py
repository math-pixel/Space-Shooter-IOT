
valueIdleX = 0
valueIdleY = 0

class GYRO():

    def __init__(self, threshold) -> None:
        self.threshold = threshold

    def process(self, valueGyro):

        valueX = "IDLE"
        valueY = "IDLE"

        # state X
        if valueGyro["x"] < valueIdleX - self.threshold:
            valueX = "right"
        elif valueGyro["x"] > valueIdleX + self.threshold:
            valueX = "left"
        else:
            valueX = "idle"

        # state Y
        if valueGyro["y"] < valueIdleY - self.threshold:
            valueY = "up"
        elif valueGyro["y"] > valueIdleY + self.threshold:
            valueY = "down"
        else:
            valueY = "idle"

        return { "x": valueX, "y":valueY }