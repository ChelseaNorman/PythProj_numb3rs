import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

# IP address should be #.#.#.# But each # should be a number between 0 and 255, inclusive
def validate(ip):
   if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        list_of_numbers_string = ip.split(".")
        for number in list_of_numbers_string:
            if int(number) < 0 or int(number) > 255:
                return False
        return True
   else:
       return False

if __name__ == "__main__":
    main()


