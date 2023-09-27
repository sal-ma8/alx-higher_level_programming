#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """jhsGdhf hui gf iughi fhgehhh fjghj.

    Args:
        my_list_1 (list): first varible in the list .
        my_list_2 (list):  sacond varible in the list.
        list_length (int): kjfsdjkhfknkv hfjhuhf hdhfjb .

    Returns:
        dvcgfdugfvjkhjh hifubghuir v rhr gih ydgfbcrvg fyuge cby.
    """
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
