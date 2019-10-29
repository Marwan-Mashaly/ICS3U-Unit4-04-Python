#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on October 2019
# This program lets user to guess a number and see if it's correct

import random

random = random.randint(1, 9+1)


def main():
    # this function lets user to guess a number and see if it's correct
    while True:
        # input
        guess_number = input("Enter a number between 0 to 9: ")
        print("")

        # process & output
        try:
            intcheck = int(guess_number)

            if intcheck == random:
                # output
                print("correct, good guess ")
                break
            else:
                print("Try Again")
                print("")
        except Exception:
            print("Invalid Number ")
            print("")


if __name__ == '__main__':
    main()
