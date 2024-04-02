import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now


class InputButton:

    def __init__(self, pin, delegate) -> None:
        GPIO.setmode(GPIO.BCM) # Use physical pin numbering
        GPIO.setup(pin, GPIO.IN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
        self.pin = pin
        self.lastState = None
        self.delegate = delegate

    def process(self):
        
        if GPIO.input(self.pin) == GPIO.HIGH : #button press


            if self.lastState != GPIO.HIGH:
                self.delegate.onClick()
                self.lastState = GPIO.HIGH
                
            
        elif GPIO.input(self.pin) == GPIO.LOW :

            if self.lastState != GPIO.LOW:
                self.delegate.onRelease()
                self.lastState = GPIO.LOW