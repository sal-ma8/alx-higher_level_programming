#!/usr/bin/python3
'''ihfsuihig uifhgufhgisghufhjah.'''


class BaseGeometry:
    '''fgiurfgnrh hg uiprhfugiwhfpiguf.'''
    def area(self):
        '''ehfhriudhg hf dijgnvfbivujbfugfqv.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Method for validating the value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
