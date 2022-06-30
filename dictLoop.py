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
            # os.system("rm -rf " + baseDirectory)
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

                # function = [key
                #             for key, value in dictOfFood.items()
                #             if user_choice == value][0]
                # function()


def listCategories():
    listOfCategories = []
    listOfFiles = (subprocess.check_output(
        ["ls --group-directories-first " + baseDirectory], shell=True).decode("utf-8")).strip().split('\n')
    for item in listOfFiles:
        # and item != "all-in-one.py" and item != "Management":
        if item != "README.md" and item != "dictLoop.py":
            listOfCategories.append(item)
    return listOfCategories


def list_to_menu(list_to_menu):
    while True:
        number = 0
        print()
        for item in list_to_menu:
            number += 1
            # if number-1 > len(list_to_menu):
            #     return
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
    print()


def Category3():
    print()


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
              Collection11: 'script11',
              Collection12: 'script12',
              Collection13: 'script13',
              Collection21: 'script21',
              Collection22: 'script22',
              Collection23: 'script23',
              Collection31: 'script31',
              Collection32: 'script32',
              Collection33: 'script33'}

# userChoice = input("Enter script name: ")


def main():

    main_menu()


if __name__ == '__main__':
    main()


# try:
#     function = [key
#                 for key, listOfValues in dictOfFood.items()
#                 if userChoice in listOfValues][0]
#     function()
# except:
#     print("Invalid Input")

    # dnsMenuCommand = "/usr/bin/python3 {}/dns_menu.py"
    # os.system(dnsMenuCommand.format(path))

    # newSiteCommand = "ansible-playbook {}/newSiteCreation.yml -e \"dest_server={} db_host={} db_password={} dest_bench={} site_name={} site_environment={} public_site_ip={} site_ip={} firewall_hostname={} proxy_server={}\""
    # os.system(newSiteCommand.format(path, destServer, dbHost, dbPassword, destBench,
    #                                 siteName, siteEnvironment, sitePublicIP, siteLocalIP, firewallHostname, proxyServer))
    # # print(newSiteCommand.format(path, destServer, dbHost, dbPassword, destBench, siteName, siteEnvironment, sitePublicIP, siteLocalIP, firewallHostname, proxyServer))
