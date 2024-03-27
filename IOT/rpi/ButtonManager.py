import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now


class InputButton:

    def __init__(self, pin, callbackOnPress, callbackOnRelease) -> None:
        GPIO.setmode(GPIO.BCM) # Use physical pin numbering
        GPIO.setup(pin, GPIO.IN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
        self.pin = pin
        self.asToggle = False
        self.lastState = None
        self.callbackOnPress = callbackOnPress
        self.callbackOnRelease = callbackOnRelease

    def process(self):
        
        if GPIO.input(self.pin) == GPIO.HIGH : #button press


            if self.lastState != GPIO.HIGH:
                self.callbackOnPress()
                self.lastState = GPIO.HIGH
                
            
        elif GPIO.input(self.pin) == GPIO.LOW :

            if self.lastState != GPIO.LOW:
                self.callbackOnRelease()
                self.lastState = GPIO.LOW