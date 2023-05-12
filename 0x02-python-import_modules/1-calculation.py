#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    total = add(a, b)
    substraction = sub(a, b)
    multiplication = mul(a, b)
    division = div(a, b)

    print(f"{a} + {b} = {total}")
    print(f"{a} - {b} = {substraction}")
    print(f"{a} * {b} = {multiplication}")
    print(f"{a} / {b} = {division}")
