import network
from SequenceTesteur import TestableClass
from Display import *

class WIFI(TestableClass):

    def __init__(self) -> None:
        pass

    @staticmethod
    def connect_wifi(ssid, password):
        wlan = network.WLAN(network.STA_IF)  # Crée un objet WLAN en mode STA
        if not wlan.isconnected():  # Vérifie si déjà connecté
            wlan.active(True)  # Active l'interface STA
            wlan.connect(ssid, password)  # Tente de se connecter au réseau
            print('Connexion au réseau', ssid)
            while not wlan.isconnected():
                pass  # Attendre jusqu'à la connexion
        print('Configuration réseau :', wlan.ifconfig())

    def testSensor(self):
        wlan = network.WLAN(network.STA_IF)  # Crée un objet WLAN en mode STA
        if wlan.isconnected():
            return DISPLAY.SUCCESS
        else:
            return DISPLAY.ERROR_SENSOR
    
