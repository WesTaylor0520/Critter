from Critter import Critter


class Dog(Critter):
    __foodLevel = 1
    __noise = "woof!"

    def sleep(self):
        Critter.sleep(self)
        print("Dog woke up! Woof!")
