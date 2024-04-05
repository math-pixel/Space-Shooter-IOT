import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from SequenceTesteur import TestableClass
from Display import *

GPIO.setwarnings(False) # Ignore warning for now


class InputButton(TestableClass):

    def __init__(self, pin, delegate) -> None:
        GPIO.setmode(GPIO.BCM) # Use physical pin numbering
        GPIO.setup(pin, GPIO.IN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
        self.pin = pin
        self.lastState = None
        self.delegate = delegate

    def testSensor(self):
        timer = 100
        while timer > 0:
            timer -= 1

            if GPIO.input(self.pin) == GPIO.HIGH : #button press
                return DISPLAY.SUCCESS
            elif GPIO.input(self.pin) == GPIO.LOW :
                pass
            
            time.sleep(0.1)

        return DISPLAY.ERROR_INPUT_USER
    
    def process(self):
        
        if GPIO.input(self.pin) == GPIO.HIGH : #button press


            if self.lastState != GPIO.HIGH:
                self.delegate.onClick()
                self.lastState = GPIO.HIGH
                
            
        elif GPIO.input(self.pin) == GPIO.LOW :

            if self.lastState != GPIO.LOW:
                self.delegate.onRelease()
                self.lastState = GPIO.LOW