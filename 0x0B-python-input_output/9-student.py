#!/usr/bin/python3
"""
GRFIHJVHDJFSDRHFBGJKFBV HGUFH IGFKFGRHGK FKFGS LH.
"""


class Student:
    """
        EFASRJF LGHSOIKLNVM'LFBV FL;KNBJRKGNRWFJOKWB 'RNBGJKRP:
        Attributes:
            first_name (str): EFBEWJOJ VLRIOYFHLBR VFIHNE.
            last_name (str): EF RJFIOHNR L[KV ;WPEFMN;W G;LWR.
            age (int): EHFGOUWJF LRPFJNLR LPHN PRN W.
        Methods:
            __init__ - RJPOFBW RGM [EWFOJWFKEKWEJD PIEO[ FPKPO.
            to_json - shfiowr gjkhiphwarbgpoj rlopJEEFB LIEBN FJJOB.
    """
    def __init__(self, first_name, last_name, age):
        """
            WRHUI RGKHG RWujopt 5t opo fjgorpogjhri.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            dhfiohgnvgklhf vnmg; lkVBRFA B ROIA GLERBQIB GLOIB.
        """
        return self.__dict__
