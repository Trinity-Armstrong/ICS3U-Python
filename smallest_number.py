#!/usr/bin/env python3

# Created by: Trinity Armstrong
# Created on: December 2019
# This program identifies the smallest of 10 random numbers


import random


def identify(array_of_numbers):
    # This function identifies the smallest number in a list

    # Variables
    smallest_number = 100

    # Process
    for counter in array_of_numbers:
        if counter < smallest_number:
            smallest_number = counter

    # Output
    return smallest_number


def main():
    # This function creates an array of 10 numbers then prints out the smallest

    # Array declaration
    random_numbers = []

    # Process
    for counter in range(10):
        number = random.randint(1, 100)
        print(number)
        random_numbers.append(number)

    # Call function
    smallest = identify(random_numbers)

    # Output
    print("")
    print("The smallest number in this array is", smallest)


if __name__ == "__main__":
    main()
