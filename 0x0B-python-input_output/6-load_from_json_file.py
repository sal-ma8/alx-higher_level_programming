#!/usr/bin/python3
"""
reihje rgfjropfkp kgjpq jrg ttb 
"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file - rjgiop p[kf jqrif rh[org.
    Args:
        filename: ehetb wryngwrtt
    """
    with open(filename, "r") as f:
        my_obj = json.load(f)
        return my_obj
