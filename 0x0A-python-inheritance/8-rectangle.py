#!/usr/bin/python3
'''DFH IDGIHFGIfui;DFH;DNDL.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''DFHIUSH OUHUARFGUOHVG.'''
    def __init__(self, width, height):
        '''dklnfSHEOG l HHdG.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
