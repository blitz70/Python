import sys
import argparse


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=float, default=1.0, help="first number")
    parser.add_argument("--y", type=float, default=1.0, help="second number")
    parser.add_argument("--operation", type=str, default="add", help="operation (add, sub, mul, div)")
    args = parser.parse_args()
    print(args)
    sys.stdout.write(str(calc_w(args)))


def calc_w(args):
    return calc(args.x, args.y, args.operation)


def calc(x, y, operation):
    if operation == "add":
        return x + y
    elif operation == "sub":
        return x + y
    elif operation == "mul":
        return x * y
    elif operation == "div":
        return x / y
    else:
        return "error"

if __name__ == "__main__":
    parse()
