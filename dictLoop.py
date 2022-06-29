def collection11():
    print("A watermelon's coming right up")


def collection12():
    print("A watermelon's coming right up")


def collection13():
    print("A watermelon's coming right up")


def collection21():
    print("A watermelon's coming right up")


def collection22():
    print("A watermelon's coming right up")


def collection23():
    print("A watermelon's coming right up")


def collection31():
    print("A watermelon's coming right up")


def collection32():
    print("A watermelon's coming right up")


def collection33():
    print("A watermelon's coming right up")


dictOfFood = {collection11: 'script11',
              collection11: 'script11',
              collection11: 'script11',
              collection21: 'script11',
              collection21: 'script11',
              collection21: 'script11',
              collection31: 'script11',
              collection31: 'script11',
              collection31: 'script11'}

userChoice = input("Enter script name: ")

try:
    function = [key
                for key, listOfValues in dictOfFood.items()
                if userChoice in listOfValues][0]
    function()
except:
    print("Invalid Input")
