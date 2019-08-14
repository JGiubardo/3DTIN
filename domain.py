from point import Point


class Domain(object):
    """Creates Class Domain."""

    def __init__(self, cx=0.0, cy=0.0, length=0.0):
        self._center_x = cx
        self._center_y = cy
        self._size = length

    def from_domain(self, quadrant: int):
        new_length = self.length/2
        # y
        if quadrant <= 1:                       # quadrant 0 and 1
            new_cy = self.cy + new_length/2
        else:                                   # quadrant 2 and 3
            new_cy = self.cy - new_length/2
        # x
        if quadrant % 3 == 0:                   # quadrant 0 and 3
            new_cx = self.cx + new_length/2
        else:                                   # quadrant 1 and 2
            new_cx = self.cx - new_length / 2
        return Domain(new_cx, new_cy, new_length)

    def subdivide(self) -> list:
        domain_list = []
        for x in range(4):
            domain_list.append(self.from_domain(x))
        return domain_list

    def point_in_boundary(self, insert_point: Point):
        return self.in_horizontal_bound(insert_point) and self.in_vertical_bound(insert_point)

    def in_horizontal_bound(self, insert_point: Point):
        left_bound = self.cx - self.length / 2
        right_bound = self.cx + self.length / 2
        return left_bound <= insert_point.x < right_bound

    def in_vertical_bound(self, insert_point: Point):
        bottom_bound = self.cy - self.length / 2
        top_bound = self.cy + self.length / 2
        return bottom_bound <= insert_point.y < top_bound

    @property
    def cx(self) -> float:
        return self._center_x

    @property
    def cy(self) -> float:
        return self._center_y

    @property
    def length(self) -> float:
        return self._size

    @property
    def center(self):
        return Point(self._center_x, self._center_y)
