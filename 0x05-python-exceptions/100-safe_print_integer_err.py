#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().

    dfhjgu  ruihr ruh uer vbi yrucuefi ieucmi.

    Args:
        value (int): dbchjgd fhfhf  fhciuh.

    Returns:
        jhdfjdc jdfjkhdkfh djhjhfj hdjchkjdweiwdiowuh
        hdkejejfdejjkdln fnedenfne fe.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
