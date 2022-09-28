import time


class Critter:
    __isAlive = True
    __foodLevel = 5
    __tiredness = 0
    winner = False
    __noise = ""

    def __init__(self, name):
        self.__name = name

    def isAlive(self):
        return self.__isAlive

    def isWinner(self):
        return self.winner

    def __die(self):
        self.__isAlive = False

    def sleep(self):
        print(f'{self.__name} sleeps.')
        for i in range(5):
            print(f"Zzz {self.__noise}")
            time.sleep(1)
        self.__tiredness = 0
        self.__foodLevel -= 3
        if self.__foodLevel <= 0:
            print(f'{self.__name} starves to death.')
            self.__die()

    def change_food(self, amount):
        self.__foodLevel += amount

    def feed(self, amount: int, food):
        if self.__isAlive:
            print(f'{self.__name} eats.')
            print(f'{self.__noise}')
            for i in range(amount):
                food.applyFood(self)
            self.__tiredness += 1
            if self.__foodLevel > 10:
                print(f'{self.__name} over ate')
                self.__die()
            elif self.__foodLevel == 10:
                print("You win!")
                self.winner = True
            elif self.__tiredness > 5:
                print(f'{self.__name} is sleepy from so much food.')
                self.sleep()
