#!/usr/bin/python3
def print_last_digit(number):
    main = number % 10
    if number < 0:
        main = (abs(number) % 10)
    print(main, end="")
    return main
