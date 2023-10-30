#!/usr/bin/python3
"""
    adlkKLFHF GKLJFOPGJF LGJPOJ FKLEROGN
"""


class Student:
    """
        fdtragfbfahtj;g rkfkgjk 'JK'elkfj; kr'pjglar;gj:
        Attributes:
            first_name (str): dfa sdgfrsehfat asgahg.
            last_name (str): fhfl;fkprdjgn fhgiojfk;dm nr.
            age (int): kejprjf rjgkfnflkeokbj fRGJOPRk.
        Methods:
            __init__ - BFKOIR VLJPEKFNLNC'BAD;'FNB  .
            to_json - ERPojngmfklgh;ok OGJPJMRD GR[oejnm.
    """
    def __init__(self, first_name, last_name, age):
        """
            ljfd'lrpub fpie[ptnm,'[e ekpekfmd .
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            aehrpOEJFN DVRP[HKM BKA BO[gkmb fblerkg[R FLWNPG W;G;JGE;LG,;.
            Args:
                attr (list): KJFIPETJOHNG VOSRJGNFKJTPRNG K JRKM;NKGR.
        """

        if attr is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__
