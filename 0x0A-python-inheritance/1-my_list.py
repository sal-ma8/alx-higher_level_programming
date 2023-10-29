#!/usr/bin/python3
'''define the file to make function that do action.'''


class MyList(list):
    '''define the class.'''
    def print_sorted(self):
        '''this is a function to print...'''
        print(sorted(self))
