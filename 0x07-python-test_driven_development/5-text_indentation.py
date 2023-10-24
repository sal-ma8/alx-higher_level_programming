#!/usr/bin/python3
"""this is the fourth file kldnfknsnk"""


def text_indentation(text):
    """this file have one method for print the text kfdnl.

    Args:
        text: the text is string hvjk.

    Raises:
        TypeError: to be solved when the error happend.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        # print(delim, text.split(delim))
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
