#!/usr/bin/env python3
def uppercase(str):
    data = ''
    for i in str:
        if ord(i) > 96 and ord(i < 123):
            data = data + chr(ord(i) - 32)
        else:
            data = data + i
        print("{}".format(data))
