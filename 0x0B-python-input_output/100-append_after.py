#!/usr/bin/python3
"""
kdjf ihs lkdhf mjphe iwo[ru hv.
"""


def append_after(filename="", search_string="", new_string=""):
    '''jdfkjhfhl jkggf ghifog h;sfjh hdufhoihr fh.'''
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            if search_string in lines[i]:
                lines[i:i + 1] = [lines[i], new_string]
                i += 1
            i += 1
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)
