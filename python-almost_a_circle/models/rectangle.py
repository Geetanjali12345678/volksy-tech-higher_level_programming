#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """Class of Rectangle"""

    number_of_instances = 0
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization method"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Setter Method of width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Getter Method of width"""
        self.__width = value

    @property
    def height(self):
        """Setter Method of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Getter Method of height"""
        self.__height = value

    @property
    def x(self):
        """Setter Method of height"""
        return self.__height

    @x.setter
    def x(self, value):
        """Getter Method of height"""
        self.__height = value

    @property
    def y(self):
        """Setter Method of height"""
        return self.__height

    @y.setter
    def y(self, value):
        """Getter Method of height"""
        self.__height = value
