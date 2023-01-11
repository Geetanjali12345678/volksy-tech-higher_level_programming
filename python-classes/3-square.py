#!/usr/bin/python3
"""class"""


class Square:
    """square size"""
    def __init__(self, size=0):
        
        try:
            if type(size) != int:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except:
            return self_size

    def area(self):
        return self.__size * * 2
