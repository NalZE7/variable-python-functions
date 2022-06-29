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
              collection12: 'script12',
              collection13: 'script13',
              collection21: 'script21',
              collection22: 'script22',
              collection23: 'script23',
              collection31: 'script31',
              collection32: 'script32',
              collection33: 'script33'}

userChoice = input("Enter script name: ")

try:
    function = [key
                for key, listOfValues in dictOfFood.items()
                if userChoice in listOfValues][0]
    function()
except:
    print("Invalid Input")
