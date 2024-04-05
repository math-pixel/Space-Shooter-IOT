import time

# Enum error Code
class DISPLAY:
    PHASE_X = "1"
    SUCCESS = "200"
    ERROR_SENSOR = "300"
    ERROR_INPUT_USER = "400"

class Displayer:

    _errors = {
        "1": {
            "name" : "Test Phase X",
            "message" : "Start phase X",
            "ledAlert" : {
                "intervalBlink" : 0.5,
                "numberBlink": None
            }
        },
        "200": {
            "name" : "succes",
            "message" : "Sensor Work Succesfully",
            "ledAlert" : {
                "intervalBlink" : 0.5,
                "numberBlink": 5
            }
        },
        "300": {
            "name" : "Error Sensor Disfonctionnement",
            "message" : "Error Sensor Disfonctionnement",
            "ledAlert" : {
                "intervalBlink" : 0.5,
                "numberBlink": 5
            }
        },
        "400": {
            "name" : "Error Input User",
            "message" : "Error Input User",
            "ledAlert" : {
                "intervalBlink" : 0.2,
                "numberBlink": 10
            }
        }
    }

    def __init__(self) -> None:
        pass

    @staticmethod
    def turnOnLed(errorInformation):
        iterator = errorInformation["ledAlert"]["numberBlink"]
        waitingTime = errorInformation["ledAlert"]["intervalBlink"]
        message = errorInformation["message"]
        for i in range(iterator):
            print(message)
            time.sleep(waitingTime)
        


    @staticmethod
    def displayErrorCode(code, numberBlink = None, intervalBlink = None):
        errorInformation = Displayer._errors[code]

        # set custom blink
        if numberBlink != None:
            errorInformation["ledAlert"]["numberBlink"] = numberBlink

        if intervalBlink != None:
            errorInformation["ledAlert"]["intervalBlink"] = intervalBlink

        if errorInformation["ledAlert"]["numberBlink"] != None and errorInformation["ledAlert"]["intervalBlink"] != None:
            Displayer.turnOnLed(errorInformation)
        else:
            print("blink iterator or interval Blink = Null")

