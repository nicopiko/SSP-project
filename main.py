import time as t
import random
import os

alcoholArray = ["alcohol1", "alcohol2", "alcohol3", "alcohol4", "alcohol5", "alcohol6", "alcohol7", "alcohol8"]
mixerArray = ["mixer1", "mixer2", "mixer3", "mixer4", "mixer5", "mixer6", "mixer7", "mixer8"]

class Mixie():
    def __init__(self):
        self.alcoholParameter = 0
        self.alcoholVolume = 0
        self.mixerParameter = 0
        self.mixerVolume = 0
        self.mixType = 0
        self.iceParameter = False

    def changeAlcohol(self):
        alcohol = input("What alcohol do you want? 1-8 ")
        amountAlcohol = input("How much of this alcohol do you want? ")
        self.alcoholParameter = int(alcohol) - 1
        self.alcoholVolume = int(amountAlcohol)

    def changeMixer(self):
        mixer = input("What mixer do you want? ")
        amountMixer = input("How much of this mixer do you want? ")
        self.mixerParameter = int(mixer) - 1
        self.mixerVolume = int(amountMixer)

    def changeMixType(self):
        mixType = input("Do you want your drink shaken(1) or stirred(2) or neither(0)? ")
        newMixType = int(mixType)
        if newMixType not in range(0,3):
            print("Invalid mix type")
            self.changeMixType()
        else:
            self.mixType = newMixType

    def getMixType(self):
        return self.mixType

    def changeIceParameter(self):
        ice = input("Do you want ice in your drink? y/n ")
        if ice == "y":
            self.iceParameter = True
        elif ice == "n":
            self.iceParameter = False

    def getIceParameter(self):
        return self.iceParameter

    def getAlcohol(self):
        alcohol = self.alcoholParameter
        amount = self.alcoholVolume
        return [alcohol, amount]

    def getMixer(self):
        mixer = self.mixerParameter
        amount = self.mixerVolume
        return [mixer, amount]


class AlcoholWheel(Mixie):
    def __init__(self):
        self.currentAlcohol = 0

    def __openValve__(self):
        print("Valve is open")

    def __closeValve__(self):
        print("Valve is closed")

    def __readFlowSensor__(self):
        return random.randint(0,5)

    def turnWheel(self):
        print(f"Current alcohol: {alcoholArray[self.currentAlcohol]}")
        t.sleep(1)
        if self.currentAlcohol < 7:
            self.currentAlcohol = self.currentAlcohol + 1
        else:
            self.currentAlcohol = 0

    def dispense(self, alcohol, amount):
        while self.currentAlcohol != alcohol + 1:
            self.turnWheel()
            if self.currentAlcohol <= alcohol:
                print("The wheel is turning...")
                t.sleep(1)
            os.system('cls')

        self.__openValve__()
        while self.__readFlowSensor__() < amount:
            t.sleep(0.5)
        t.sleep(0.5)
        self.__closeValve__()
        t.sleep(1)


class MixerWheel(Mixie):
    def __init__(self):
        self.currentMixer = 0

    def __openValve__(self):
        print("Valve is open")

    def __closeValve__(self):
        print("Valve is closed")

    def __readFlowSensor__(self):
        return random.randint(0, 5)

    def turnWheel(self):
        print(f"Current mixer: {mixerArray[self.currentMixer]}")
        t.sleep(1)
        if self.currentMixer < 7:
            self.currentMixer = self.currentMixer + 1
        else:
            self.currentMixer = 0

    def dispense(self, mixer, amount):
        while self.currentMixer != mixer + 1:
            self.turnWheel()
            if self.currentMixer <= mixer:
                print("Wheel is turning...")
                t.sleep(1)
            os.system('cls')

        self.__openValve__()
        while self.__readFlowSensor__() < amount:
            t.sleep(0.5)
        t.sleep(0.5)
        self.__closeValve__()
        t.sleep(1)

class Shaker(Mixie):
    def __shake__(self):
        print("Shaking drink...")
        t.sleep(1)

    def __stir__(self):
        print("Stirring drink...")
        t.sleep(1)

    def mix(self):
        if Mixie.getMixType() == 0:
            pass
        elif Mixie.getMixType() == 1:
            self.__shake__()
        elif Mixie.getMixType() == 2:
            self.__stir__()

class Transport(Mixie):
    def dispenseCup(self):
        print("Dispensing cup...")
        t.sleep(1)

    def dispenseIce(self):
        if Mixie.getIceParameter():
            print("Dispensing ice...")
            t.sleep(1)

    def goToAlcohol(self):
        print("Moving cup to the alcohol wheel...")
        t.sleep(1)

    def goToMixer(self):
        print("Moving cup to the mixer wheel...")
        t.sleep(1)

    def goToShaker(self):
        print("Moving cup to shaker...")
        t.sleep(1)

    def serveDrink(self):
        print("Drink is ready, hope it tastes! :3")

Mixie = Mixie()
alcoholWheel = AlcoholWheel()
mixerWheel = MixerWheel()
shaker = Shaker()
transport = Transport()

#Choose alcohol
Mixie.changeAlcohol()
os.system('cls')

#Choose mixer
Mixie.changeMixer()
os.system('cls')

#Choose ice
Mixie.changeIceParameter()
os.system('cls')

#Choose mixtype
Mixie.changeMixType()
os.system('cls')

#Display choices
print("Current drink parameters:")
if Mixie.getIceParameter():
    if Mixie.getMixType() == 1:
        print(f"{Mixie.getAlcohol()[1]} ml of {alcoholArray[Mixie.getAlcohol()[0]]} combined with {Mixie.getMixer()[1]} ml of {mixerArray[Mixie.getMixer()[0]]} shaken with ice. Sounds delicious, coming right up! :3")
    elif Mixie.getMixType() == 2:
        print(f"{Mixie.getAlcohol()[1]} ml of {alcoholArray[Mixie.getAlcohol()[0]]} combined with {Mixie.getMixer()[1]} ml of {mixerArray[Mixie.getMixer()[0]]} stirred with ice. Sounds delicious, coming right up! :3")
    else:
        print(f"{Mixie.getAlcohol()[1]} ml of {alcoholArray[Mixie.getAlcohol()[0]]} combined with {Mixie.getMixer()[1]} ml of {mixerArray[Mixie.getMixer()[0]]} with ice. Sounds delicious, coming right up! :3")
else:
    if Mixie.getMixType() == 1:
        print(f"{Mixie.getAlcohol()[1]} ml of {alcoholArray[Mixie.getAlcohol()[0]]} combined with {Mixie.getMixer()[1]} ml of {mixerArray[Mixie.getMixer()[0]]} shaken. Sounds delicious, coming right up! :3")
    elif Mixie.getMixType() == 2:
        print(f"{Mixie.getAlcohol()[1]} ml of {alcoholArray[Mixie.getAlcohol()[0]]} combined with {Mixie.getMixer()[1]} ml of {mixerArray[Mixie.getMixer()[0]]} stirred. Sounds delicious, coming right up! :3")
    else:
        print(f"{Mixie.getAlcohol()[1]} ml of {alcoholArray[Mixie.getAlcohol()[0]]} combined with {Mixie.getMixer()[1]} ml of {mixerArray[Mixie.getMixer()[0]]}. Sounds delicious, coming right up! :3")

#Make drink
t.sleep(5)
transport.dispenseCup()
os.system('cls')
transport.dispenseIce()
os.system('cls')

transport.goToAlcohol()
os.system('cls')
alcoholWheel.dispense(Mixie.getAlcohol()[0], Mixie.getAlcohol()[1])

transport.goToMixer()
os.system('cls')
mixerWheel.dispense(Mixie.getMixer()[0], Mixie.getMixer()[1])

if Mixie.getMixType() != 0:
    transport.goToShaker()
    os.system('cls')
    shaker.mix()
    os.system('cls')

transport.serveDrink()
t.sleep(5)