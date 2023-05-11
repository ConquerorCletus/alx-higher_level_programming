#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    from sys import argv, exit

    av = argv
    ac = len(av)

    if ac != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    a = int(av[1])
    b = int(av[3])
    operators = {'+', '-', '*', '/'}

    if av[2] not in operators:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    if av[2] == '+':
        print('{:} + {:d} = {:d}'.format(a, b, add(a, b)))
    elif av[2] == '-':
        print('{:} - {:d} = {:d}'.format(a, b, sub(a, b)))
    elif av[2] == "*":
        print('{:} * {:d} = {:d}'.format(a, b, mul(a, b)))
    elif av[2] == '/':
        print('{:} / {:d} = {:d}'.format(a, b, div(a, b)))
