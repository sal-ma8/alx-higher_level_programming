#!/usr/bin/python3

if __name__ == "__main__":
    """the function def add(a, b): from the file add_0.py 
    and prints the result of the addition."""
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
