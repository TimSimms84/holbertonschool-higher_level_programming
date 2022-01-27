#!/usr/bin/python3
"""
Square that inhertis from Rectangle class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """Returns a dictionary rep of a square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def update(self, *args, **kwargs):
        attrs, i = ['id', 'size', 'x', 'y'], 0
        if args:
            for value in args:
                setattr(self, attrs[i], value)
                i += 1
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """custom __str__ method for Square
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}\
 - {self.width}"

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
