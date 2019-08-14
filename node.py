from domain import Domain
from point import Point


class Node(object):
    """Creates Class node"""
    def __init__(self, d: Domain):
        self._dom = d
        self._type = "empty"
        self.index_list = []
        self.triangle_index_set = set()
        self._NE = None
        self._NW = None
        self._SW = None
        self._SE = None

    def contains_point(self, insert_point: Point):
        return self._dom.point_in_boundary(insert_point)

    def point_in_node_list(self, p: Point, point_list: list) -> bool:
        for p_index in self.index_list:
            a_point = point_list[p_index]
            if a_point.equals(p):
                return True       # Else continue
        return False

    def add_triangle(self, t: int, node_label: int):
        if t not in self.triangle_index_set:
            self.triangle_index_set.add(t)
            print("   Into node: " + str(node_label))

    def add_point(self, p: int):
        if self.has_children:
            raise Exception("Tried to add a point to an internal node")
        else:
            self.index_list.append(p)
            if self.is_empty:
                self._type = "full"

    def add_children(self, point_list):
        """Creates children and sends the points in the node to them"""
        quadrants = self._dom.subdivide()
        self._NE = Node(quadrants.pop(0))
        self._NW = Node(quadrants.pop(0))
        self._SW = Node(quadrants.pop(0))
        self._SE = Node(quadrants.pop(0))
        self._type = "parent"
        self.points_to_children(point_list)

    def points_to_children(self, point_list):
        """Takes the points in a node and sends them to it's children, called when a node becomes a parent"""
        for i in self.index_list:
            p = point_list[i]
            if self._dom.center.x < p.x:
                if self._dom.center.y < p.y:
                    self._NE.add_point(i)
                else:
                    self._SE.add_point(i)
            else:
                if self._dom.center.y < p.y:
                    self._NW.add_point(i)
                else:
                    self._SW.add_point(i)
        self.index_list = []

    def visit(self, node_label):
        """Provides a print out of the contents of the node"""
        visit_string = "    Node " + str(node_label) + ": " + self._type
        if self.is_full:
            visit_string += ": \n      Points: "
            for p in self.index_list:
                visit_string += str(p) + " "
            visit_string += "\n      Triangles: "
            for t in self.triangle_index_set:
                visit_string += str(t) + " "
        print(visit_string)

    @property
    def num_points_inside(self):
        return len(self.index_list)

    @property
    def is_empty(self):
        return self._type == "empty"

    @property
    def is_full(self):
        return self._type == "full"

    @property
    def has_children(self):
        return self._type == "parent"

    @property
    def center_point(self):
        return self._dom.center

    @property
    def child_list(self):
        if self.has_children:
            return [self._NE, self._NW, self._SW, self._SE]
        else:
            return []

    def child(self, quadrant: int):
        return self.child_list[quadrant]
