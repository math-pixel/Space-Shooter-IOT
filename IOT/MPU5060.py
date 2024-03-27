
valueIdleX = 0
valueIdleY = 0

class GYRO():

    def __init__(self, threshold) -> None:
        self.threshold = threshold

    def process(self, valueGyro):

        valueX = "IDLE"
        valueY = "IDLE"

        # state X
        if valueGyro.x < valueIdleX - self.threshold:
            valueX = "LEFT"
        elif valueGyro.x > valueIdleX + self.threshold:
            valueX = "RIGHT"
        else:
            valueX = "IDLE"

        # state Y
        if valueGyro.y < valueIdleY - self.threshold:
            valueY = "DOWN"
        elif valueGyro.y > valueIdleY + self.threshold:
            valueY = "UP"
        else:
            valueY = "IDLE"

        return '{ "x":"' + valueX + '", "y":"'+ valueY +'"}'