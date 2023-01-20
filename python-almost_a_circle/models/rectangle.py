#!/usr/bin/python3

"""

Rectangle Class

"""







class Rectangle:

    """Class of Rectangle"""




    number_of_instances = 0

    print_symbol = "#"




    """class defined"""

    def __init__(self, width=0, height=0):

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

        if isinstance(value, int) is False:

            raise TypeError('width must be an integer')

        if value < 0:

            raise TypeError('width must be >= 0')

        self.__width = value




    @property

    def height(self):

        """Setter Method of height"""

        return self.__height




    @height.setter

    def height(self, value):

        """Getter Method of height"""

    def area(self):

        """method to return area of width and height"""

        return self.__width * self.__height




    def perimeter(self):

        """method to return perimeter of width and height"""

        if self.__width == 0 or self.__height == 0:

            return 0

        return (self.__width + self.__height) * 2




    @staticmethod

    def bigger_or_equal(rect_1, rect_2):

        """returns the biggest rectangle area"""

        if isinstance(rect_1, Rectangle) is False:

            raise TypeError('rect_1 must be an instance of Rectangle')

        if isinstance(rect_2, Rectangle) is False:

            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() > rect_2.area():

            return rect_1

        if rect_1.area() < rect_2.area():

            return rect_2

        return rect_1




    def __str__(self):

        """method string object"""

        if self.__width == 0 or self.__height == 0:

            return ""

        for row in range(self.__height - 1):

            print(str(self.print_symbol) * self.__width)

        return str(str(self.print_symbol) * self.__width)




    def __repr__(self):

        """repr method"""

        return ("Rectangle({}, {})".format(self.__width, self.__height))




    def __del__(self):

        """delete object/instance"""

        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

dibyakanti dhir, Yesterday 10:45 AM
#!/usr/bin/python3
"""here module is documented"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        values = load_from_json_file('add_item.json')
    except FileNotFoundError:
        values = []
    for i in sys.argv[1:]:
        values.append(i)
    save_to_json_file(values, 'add_item.json')

dibyakanti dhir, Yesterday 10:57 PM
#!/usr/bin/python3

"""module is documented"""


