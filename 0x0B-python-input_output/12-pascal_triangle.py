#!/usr/bin/python3
"""
rhlijrj vrijtoropvrp[jjckr .
"""


def pascal_triangle(n):
    """
    rehglrehglj;gjnhklnflkhjl;djlbf;kwrkgprojp[rkgnbjkprt
        Args:
            n (int): fdhglhdl;gnd
        Returns: rgbrlkfgler
    """
    rows = [[1 for j in range(i + 1)] for i in range(n)]
    for n in range(n):
        for i in range(n - 1):
            rows[n][i + 1] = sum(rows[n - 1][i:i + 2])
    return rows
