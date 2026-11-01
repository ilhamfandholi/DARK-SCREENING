
import os
from modules.report_generator import generate_report
from modules.username_search import username_search
from modules.ip_lookup import ip_lookup
from modules.geo_location import geo_location
from modules.dns_scanner import dns_scanner
from modules.name_search import name_search

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"


def clear():
    os.system("cls")


def banner():
    print(GREEN + r"""
 ____    _    ____  _  __
|  _ \  / \  |  _ \| |/ /
| | | |/ _ \ | |_) | ' /
| |_| / ___ \|  _ <| . \
|____/_/   \_\_| \_\_|\_\

       DARK SCREENING
       MULTI SCANNER v1.0
""" + RESET)


def menu():
    print(CYAN + """
 [1] IP ADDRESS LOOKUP
 [2] GEO LOCATION
 [3] DNS SCANNER
 [4] NAME SEARCH
 [5] USERNAME SEARCH
 [6] GENERATE REPORT

 [0] EXIT
""" + RESET)


def main():
    while True:
        clear()
        banner()
        menu()

        choice = input(" DARK-SCREENING >> ")

        if choice == "1":
            ip_lookup()

        elif choice == "2":
            geo_location()

        elif choice == "3":
            dns_scanner()

        elif choice == "4":
            name_search()

        elif choice == "5":
             username_search()

        elif choice == "6":
             generate_report()

        elif choice == "0":
            print("SYSTEM EXIT...")
            break

        else:
            print(RED + "INVALID OPTION!" + RESET)

        input("\nPress ENTER to continue...")


if __name__ == "__main__":
    main()
