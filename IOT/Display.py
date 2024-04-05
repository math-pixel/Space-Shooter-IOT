import time
class Displayer:

    _errors = {
        "1": {
            "name" : "Test Phase X",
            "ledAlert" : {
                "intervalBlink" : 1,
                "numberBlink": None
            }
        },
        "42": {
            "name" : "succes",
            "ledAlert" : {
                "intervalBlink" : 0.5,
                "numberBlink": 5
            }
        },
        "404": {
            "name" : "Error",
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
        for i in range(iterator):
            print("led On")
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

