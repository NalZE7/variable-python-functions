def battikhaHamra():
    print("A watermelon's coming right up")


def jebnehBeedah():
    print("A plate of whitecheese for you")


def summerSpecial():
    print("This is the ultimate dish!")


dictOfFood = {battikhaHamra: ['battikha', 'watermelon'],
              jebnehBeedah: ['jebneh', 'jebneh beedah', 'whitecheese'],
              summerSpecial: ['both', 'special', 'summer breeze']}

userChoice = input("Would you like to eat watermelon or whitecheese? ")

try:
    function = [key
                for key, listOfValues in dictOfFood.items()
                if userChoice in listOfValues][0]
    function()
except:
    print("Invalid Input")
