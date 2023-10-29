#!/usr/bin/python3
'''fgur ahod[peir - rihvhvofia.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''dfhgfg dhfjdpohfoihedf.'''
    def __init__(self, size):
        '''fhsiugui fugijhaifdhuif auip.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''dfadgfd df grg fgh.'''
        return self.__size ** 2
