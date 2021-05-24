#!/usr/bin/env python3

# Created by Brian Musembi
# Created on May 2021
# This program converts temperature from °Celsius to °Fahrenheit


def fahrenheit():
    # this function converts temperature from °Celsius to °Fahrenheit

    # input
    celsius_temp = input("Input a temperature in degrees celsius(°C): ")
    print("")

    # process
    try:
        celsius_temp_int = int(celsius_temp)

        fahrenheit_temp = (9 / 5) * celsius_temp_int + 32

        # output
        print("{0}°C is equal to {1}°F."
              .format(celsius_temp_int, fahrenheit_temp))
    except Exception:
        # output
        print("{} not a temperature! Please try again.".format(celsius_temp))


def main():
    # calls other functions

    # fahrenheit function
    fahrenheit()


if __name__ == "__main__":
    main()
