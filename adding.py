#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Sept 2020
# This is the adding program, in python


def main():
    # this function adds all integers from 1 to the entered number

    # this is to keep track of how many times it goes in a loop
    while_loop = 0
    total = 0

    # input
    user_as_string = input("Enter a positive integer: ")

    try:
        # convert string to integer
        user_input = int(user_as_string)

        # process and output
        while while_loop <= user_input:
            total = total + while_loop
            while_loop = while_loop + 1

        print("The sum from the integers 1 to {0} is {1}".format(user_as_string, total))

    except Exception:
        print("{0} is an invalid input.".format(user_as_string))
    print("\nDone.")


if __name__ == "__main__":
    main()
