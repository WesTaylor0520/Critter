from Critter import Critter


class Cat(Critter):
    __tiredness = 3
    __noise = "Meow!"

    def feed(self, amount: int, food):
        print("Cat is hungry!")
        Critter.feed(self, amount, food)

