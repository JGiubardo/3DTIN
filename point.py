from math import fabs


class Point(object):
    """Creates Class Point."""
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z

    def equals(self, p):
        small = .000001   # gives a precision that should stop floating point errors until very large x,y
        return fabs(p.x-self.x) < small and fabs(p.y-self.y) < small and fabs(p.z-self.z) < small

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @property
    def to_string(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.z) + " "

    def is_higher(self, p):
        return self.z > p.z

    def is_lower(self, p):
        return self.z < p.z
