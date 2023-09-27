#!/usr/bin/python3

def safe_print_division(a, b):
    """Return natg ksmt rkmeen almkam lysa zero."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
