#!/usr/bin/python3
"""
Square class
"""


class Square():
    """Documentation"""
    width = height = 0

    def __init__(self, size=None):
        """Documentation"""
        self.height = self.width = size

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Perimetre of square definition"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Return a string representation of a square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(size=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
