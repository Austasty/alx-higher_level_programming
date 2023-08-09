#!/usr/bin/python3
k = 0
for l in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(l- k)), end="")
    k = 32 if k == 0 else 0
