#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """function to print x list named save.

    Args:
        my_list (list): the frist varible list.
        x (int): second varble x its type is integer.

    Returns:
        som number in list named list its type integer.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
