#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print t dfbgh dbgvyuegf gdyfvgyuge fgdyufvgyu.

    Args:
        my_list (list): sdfgh jkd safv.
        x (int): scfdghvj bskd fbvjshdf ffdvugeyfg dffeh.

    Returns:
        hgfhcj sdnkg lfjhdjskfmls hdi hjvdjfkhjdcbghk.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
