#!/usr/bin/python3
'''fioqe fjopqk fpvjfpqfjivoof;hqo;hq f.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''rhfioqr fopr fpor porfirufjoir.'''
    def __init__(self, size):
        '''hfoqh wofjpeof'pkeof]jrojj.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''ehofiwhe ifjripjfopfue jfjfp.'''
        return self.__size ** 2

    def __str__(self):
        '''ekfhiohfohfio fhoqifoq[jf oqrjfiorfj;phrfoh f.'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
