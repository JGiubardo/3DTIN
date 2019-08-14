from point import Point


class Triangle(object):
    def __init__(self, v1: int, v2: int, v3: int):
        self._points = [v1, v2, v3]

    def get_point(self, index: int, point_list: list) -> Point:
        return point_list[self._points[index]]

    @property
    def all_points(self):
        return self._points

    @property
    def to_string(self) -> str:
        return str(self.all_points[0]) + "," + str(self.all_points[1]) + "," + str(self.all_points[2])
