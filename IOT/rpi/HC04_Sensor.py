import RPi.GPIO as GPIO
import time
from SequenceTesteur import *
from Display import *
import time

# Définir les broches du capteur
TRIG = 23
ECHO = 24
class HC04_Sensor(TestableClass):

    def __init__(self, trig, echo) -> None:
        self.trig = trig
        self.echo = echo

    def setupSensor(self):
        # Utiliser la numérotation BCM pour les broches GPIO
        GPIO.setmode(GPIO.BCM)

        # Définir TRIG comme une broche de sortie
        GPIO.setup(self.trig, GPIO.OUT)
        # Définir ECHO comme une broche d'entrée
        GPIO.setup(self.echo, GPIO.IN)

    def testSensor(self):

        time.sleep(5)
        
        distance = self.get_distance()
        if distance > 5 and distance < 10:
            return DISPLAY.SUCCESS
        else:
            return DISPLAY.ERROR_INPUT_USER

    def get_distance(self):
        # Envoyer une impulsion ultrasonique
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        start_time = time.time()
        stop_time = time.time()

        # Enregistrer le temps de début
        while GPIO.input(self.echo) == 0:
            start_time = time.time()

        # Enregistrer le temps d'arrêt
        while GPIO.input(self.echo) == 1:
            stop_time = time.time()

        # Calculer la durée de l'impulsion ultrasonique
        elapsed_time = stop_time - start_time

        # Calculer la distance en utilisant la vitesse du son (343m/s)
        # La distance est la moitié de la durée de l'impulsion multipliée par la vitesse du son
        distance = (elapsed_time * 34300) / 2

        return distance

def cleanup():
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        sensor = HC04_Sensor(TRIG, ECHO)
        sensor.setupSensor()
        while True:
            distance = sensor.get_distance()
            print("Distance:", distance, "cm")
            time.sleep(1)
    except KeyboardInterrupt:
        cleanup()
