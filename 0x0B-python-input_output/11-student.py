#!/usr/bin/python3
'''fdtygfjh jddhnsygh xdtffds yskksj hhjjkd.'''


class Student:
    '''dtydxghs  yhsjh jhjsuhgghj hjs.'''
    def __init__(self, first_name, last_name, age):
        '''dftyt sg hyhtuysj j twj.'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''srdtrseysdh tht thyr htht ss.'''
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        '''fnglkjfojritpnbjbkjthhahhteeh tg.'''
        for key, value in json.items():
            self.__dict__[key] = value
