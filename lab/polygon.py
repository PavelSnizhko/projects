from math import fabs, tan

from projects.lab.annotaion import check_values
from projects.lab.interfacePolygon import PolygonInterface
from projects.lab.point import Point


class Polygon(Point, PolygonInterface):
    __closure__ = None

    def __init__(self, x: int, y, n, a):
        super().__init__(x, y)
        self.__n = n
        self.__a = a

    def calculate_square(self):
        return self.__n * self.__a ** 2 / 4.0 * fabs(tan(180 / float(self.__n)))

    def get_n(self):
        return self.__n

    @check_values
    def set_n(self, n: int):
        print("fd")
        self.__n = n

    def get_a(self):
        return self.__a

    @check_values
    def set_a(self, a):
        self.__a = a
        print(self.__a)

    def __str__(self):
        return "Square of polygon is " + str(self.calculate_square())