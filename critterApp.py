from Critter import Critter
from Cat import Cat
from Dog import Dog
from Food import Banana, Poison


def main():
    critter = input("Cat or dog?")
    if critter == "Cat":
        bob = Cat(input("Enter a name for your Cat "))
    else:
        bob = Dog(input("Enter a name for your Dog"))

    while bob.isAlive() and not bob.isWinner():
        action = input('What would you like Critter to do?')
        if action == 'eat':
            amount = int(input("How much food? "))
            food_type = input("Banana or poison?")
            if food_type == "Banana":
                food = Banana()
            else:
                food = Poison()
            bob.feed(amount, food)
        elif action == 'sleep':
            bob.sleep()
    if not bob.isWinner():
        print("Critter has died!")
    else:
        print("You win!")


if __name__ == '__main__':
    main()
