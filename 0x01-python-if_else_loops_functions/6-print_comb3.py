#!/usr/bin/python3
for dig in range(0, 10):
    for digit in range(dig + 1, 10):
        if dig == 8 and digit == 9:
            print("{}{}".format(digit1, digit2))
        else:
            print("{}{}".format(digit1, digit2), end=", ")
