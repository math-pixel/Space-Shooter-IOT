import RPi.GPIO as GPIO
import time

# Définir les broches du capteur
TRIG = 23
ECHO = 24

def setupHC04Sensor():
    # Utiliser la numérotation BCM pour les broches GPIO
    GPIO.setmode(GPIO.BCM)

    # Définir TRIG comme une broche de sortie
    GPIO.setup(TRIG, GPIO.OUT)
    # Définir ECHO comme une broche d'entrée
    GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    # Envoyer une impulsion ultrasonique
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start_time = time.time()
    stop_time = time.time()

    # Enregistrer le temps de début
    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    # Enregistrer le temps d'arrêt
    while GPIO.input(ECHO) == 1:
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
        setupHC04Sensor()
        while True:
            distance = get_distance()
            print("Distance:", distance, "cm")
            time.sleep(1)
    except KeyboardInterrupt:
        cleanup()
