#!/usr/bin/python3

"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.

    Attributes:
    - __width (int): The width of the rectangle.
    - __height (int): The height of the rectangle.

    Methods:
    - __init__(self, width, height): Initializes a new Rectangle instance.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.

        Raises:
        - TypeError: If width or height is not an integer.
        - ValueError: If width or height is not greater than 0.
        """
        super().__init__()

        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
