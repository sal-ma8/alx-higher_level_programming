#!/usr/bin/python3
"""fjnroejgkn kgmtkgmbkg djgohngjho njfrg ."""


def add_attribute(obj, att, value):
    """iorewhgjtpj qekrjg irejgijvgowk jqrojnkfkj kfninfing.
    Args:
        obj (any): wrhfouqhg firhiorfh [govqri r[o.
        att (str): rfuhquirehfief iehiofhqoh afiohqfh rhio.
        value (any): rhfoihewiojrfoewh fciohifjrjfjr.
    Raises:
        TypeError: jhhvfoahrgj oprjogpu  pjogopvjojrp[k po.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
