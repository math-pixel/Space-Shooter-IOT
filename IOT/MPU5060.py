
valueIdleX = 0
valueIdleY = 0

class GYRO():

    def __init__(self, threshold) -> None:
        self.threshold = threshold

    def process(self, valueGyro):
        
        # state X
        if valueGyro.x < valueIdleX - self.threshold:
            pass
        elif valueGyro.x > valueIdleX + self.threshold:
            pass

        # state Y
        if valueGyro.y < valueIdleY - self.threshold:
            pass
        elif valueGyro.y > valueIdleY + self.threshold:
            pass

    
