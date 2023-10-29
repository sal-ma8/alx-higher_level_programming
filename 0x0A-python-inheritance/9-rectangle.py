#!/usr/bin/python3
'''HJ GGYGGG HHFGY GYF FYFY.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''FDHSAFJHA JFGHVOFFAF.'''
    def __init__(self, width, height):
        '''dfbkGD FDFJ DB;FDVF.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''ugi giguyfyuf ufuy  ygh.'''
        return self.__width * self.__height

    def __str__(self):
        '''Skfhgkjhf hgjhfgafv ffg.'''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
