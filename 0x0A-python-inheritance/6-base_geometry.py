#!/usr/bin/python3
"""An class that has a public method"""


class BaseGeometry:
    ''' it has a public method'''
    def area(self):
        ''' that raises an Exception with a message'''
        raise Exception("area() is not implemented")
