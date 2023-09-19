#!/usr/bin/python3

class Square:
    side_length = 0

    def __init__(self, side_length=0):
        self.side_length = side_length

    def area_of_my_square(self):
        """ Area of square """
        return self.side_length * self.side_length

    def perimeter_of_my_square(self):
        """ Perimeter"""
        return 4 * self.side_length

    def __str__(self):
        return str(self.side_length)


if __name__ == "__main__":
    s = Square(side_length=12)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())
