import os
import subprocess
from time import sleep

baseDirectory = "/opt/variable-python-functions"


def main_menu():
    while True:
        listOfCategories = listCategories()
        list_to_menu(listOfCategories)
        try:
            user_choice = int(input("\n>>> Enter option number: "))
        except:
            print("Please enter a valid Input from the list")
            sleep(1)
            continue

        if user_choice == 0:
            print("This option is reserved for special cases and not used yet")
            sleep(1)
            continue
        # exit the while loop and the whole script
        if user_choice == 99:
            print("Exiting...")
            break
        elif user_choice > len(listOfCategories) or user_choice < 0:
            print("Please enter a valid Input from the list")
            sleep(1)
            continue

        index = (int(user_choice) - 1)
        for category in listOfCategories:
            if category == listOfCategories[index]:
                function = [k
                            for k, v in dictOfFood.items()
                            if v == category][0]
                function()


def listCategories():
    listOfCategories = []
    listOfFiles = (subprocess.check_output(
        ["ls --group-directories-first " + baseDirectory], shell=True).decode("utf-8")).strip().split('\n')
    for item in listOfFiles:
        if item != "README.md" and item != "dictLoop.py":
            listOfCategories.append(item)
    return listOfCategories


def list_to_menu(list_to_menu):
    while True:
        number = 0
        print()
        for item in list_to_menu:
            number += 1
            print(str(number) + ".", item)
        print("\n99. Back\n")
        break


def listWhatsInside(choice):
    listOfFiles = (subprocess.check_output(
        ["ls --group-directories-first " + baseDirectory + "/" + choice], shell=True).decode("utf-8")).strip().split('\n')
    return listOfFiles


def Category1():
    path = "Category1/"
    listOfWhatsInside = listWhatsInside(path)
    while True:
        list_to_menu(listOfWhatsInside)
        try:
            user_choice = int(input("\n>>> Enter option number: "))
        except:
            print("Please enter a valid Input from the list")
            sleep(1)
            continue
        if user_choice == 0:
            print("This option is reserved for special cases and not used yet")
            sleep(1)
            continue

        # exit the while loop and the whole script
        if user_choice == 99:
            break
        elif user_choice > len(listOfWhatsInside) or user_choice < 0:
            print("Please enter a valid Input from the list")
            sleep(1)
            continue

        index = (int(user_choice) - 1)
        for category in listOfWhatsInside:
            if category == listOfWhatsInside[index]:
                function = [k for k, v in dictOfFood.items()
                            if v == category][0]
                function()


def Category2():
    path = "Category2/"
    listOfWhatsInside = listWhatsInside(path)
    while True:
        list_to_menu(listOfWhatsInside)
        try:
            user_choice = int(input("\n>>> Enter option number: "))
        except:
            print("Please enter a valid Input from the list")
            sleep(1)
            continue
        if user_choice == 0:
            print("This option is reserved for special cases and not used yet")
            sleep(1)
            continue

        # exit the while loop and the whole script
        if user_choice == 99:
            break
        elif user_choice > len(listOfWhatsInside) or user_choice < 0:
            print("Please enter a valid Input from the list")
            sleep(1)
            continue

        index = (int(user_choice) - 1)
        for category in listOfWhatsInside:
            if category == listOfWhatsInside[index]:
                function = [k for k, v in dictOfFood.items()
                            if v == category][0]
                function()


def Category3():
    path = "Category3/"
    listOfWhatsInside = listWhatsInside(path)
    while True:
        list_to_menu(listOfWhatsInside)
        try:
            user_choice = int(input("\n>>> Enter option number: "))
        except:
            print("Please enter a valid Input from the list")
            sleep(1)
            continue
        if user_choice == 0:
            print("This option is reserved for special cases and not used yet")
            sleep(1)
            continue

        # exit the while loop and the whole script
        if user_choice == 99:
            break
        elif user_choice > len(listOfWhatsInside) or user_choice < 0:
            print("Please enter a valid Input from the list")
            sleep(1)
            continue

        index = (int(user_choice) - 1)
        for category in listOfWhatsInside:
            if category == listOfWhatsInside[index]:
                function = [k for k, v in dictOfFood.items()
                            if v == category][0]
                function()


def Collection11():
    path = baseDirectory + "/Category1/Collection11"

    dnsMenuCommand = "/usr/bin/python3 {}/script11.py"
    os.system(dnsMenuCommand.format(path))


def Collection12():
    path = baseDirectory + "/Category1/Collection12"

    dnsMenuCommand = "/usr/bin/python3 {}/script12.py"
    os.system(dnsMenuCommand.format(path))


def Collection13():
    path = baseDirectory + "/Category1/Collection13"

    dnsMenuCommand = "/usr/bin/python3 {}/script13.py"
    os.system(dnsMenuCommand.format(path))


def Collection21():
    path = baseDirectory + "/Category2/Collection21"

    dnsMenuCommand = "/usr/bin/python3 {}/script21.py"
    os.system(dnsMenuCommand.format(path))


def Collection22():
    path = baseDirectory + "/Category2/Collection22"

    dnsMenuCommand = "/usr/bin/python3 {}/script22.py"
    os.system(dnsMenuCommand.format(path))


def Collection23():
    path = baseDirectory + "/Category2/Collection23"

    dnsMenuCommand = "/usr/bin/python3 {}/script23.py"
    os.system(dnsMenuCommand.format(path))


def Collection31():
    path = baseDirectory + "/Category3/Collection31"

    dnsMenuCommand = "/usr/bin/python3 {}/script31.py"
    os.system(dnsMenuCommand.format(path))


def Collection32():
    path = baseDirectory + "/Category3/Collection32"

    dnsMenuCommand = "/usr/bin/python3 {}/script32.py"
    os.system(dnsMenuCommand.format(path))


def Collection33():
    path = baseDirectory + "/Category3/Collection33"

    dnsMenuCommand = "/usr/bin/python3 {}/script33.py"
    os.system(dnsMenuCommand.format(path))


dictOfFood = {Category1:    'Category1',
              Category2:    'Category2',
              Category3:    'Category3',
              Collection11: 'Collection11',
              Collection12: 'Collection12',
              Collection13: 'Collection13',
              Collection21: 'Collection21',
              Collection22: 'Collection22',
              Collection23: 'Collection23',
              Collection31: 'Collection31',
              Collection32: 'Collection32',
              Collection33: 'Collection33'}


def main():

    main_menu()


if __name__ == '__main__':
    main()

