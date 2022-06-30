import os


baseDirectory = "/opt/variable-python-functions"


def collection11():
    path = baseDirectory + "/Category1/Collection11"

    dnsMenuCommand = "/usr/bin/python3 {}/script11.py"
    os.system(dnsMenuCommand.format(path))


def collection12():
    print("script12")


def collection13():
    print("script13")


def collection21():
    print("script21")


def collection22():
    print("script22")


def collection23():
    print("script23")


def collection31():
    print("script31")


def collection32():
    print("script32")


def collection33():
    print("script33")


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

    dnsMenuCommand = "/usr/bin/python3 {}/dns_menu.py"
    os.system(dnsMenuCommand.format(path))

    newSiteCommand = "ansible-playbook {}/newSiteCreation.yml -e \"dest_server={} db_host={} db_password={} dest_bench={} site_name={} site_environment={} public_site_ip={} site_ip={} firewall_hostname={} proxy_server={}\""
    os.system(newSiteCommand.format(path, destServer, dbHost, dbPassword, destBench,
                                    siteName, siteEnvironment, sitePublicIP, siteLocalIP, firewallHostname, proxyServer))
    # print(newSiteCommand.format(path, destServer, dbHost, dbPassword, destBench, siteName, siteEnvironment, sitePublicIP, siteLocalIP, firewallHostname, proxyServer))
