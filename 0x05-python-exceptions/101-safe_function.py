#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """fbjh nuhgviuy hb hvgurh jghr gu.

    Args:
        fct: fjh gfgh  ufghufhhf hh.
        args: fg ahgkfdjhjdjf s hdf.

    Returns:
        shfuhi huidhfuui hr uhe euiy ue gfg hfgh.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)

