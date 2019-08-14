from node import Node
from point import Point
from triangle import Triangle


def preorder(node: Node, node_label):
    """Provides an output of the tree into standard output using preorder traversal"""
    counter = node_label * 4
    node.visit(node_label)
    if node.has_children:
        for children in node.child_list:
            counter += 1
            preorder(children, counter)


def quadrant_selector(center: Point, search_point: Point, node_label) -> (int, int):
    """"Takes a point and discovers which of the 4 quadrants it lies in based on the center of the square
        Returns both the quadrant as a number in respect to center, and a label for the node that represents that region
    """
    if center.x <= search_point.x:
        if center.y <= search_point.y:
            return 0, 4 * node_label + 1
        else:
            return 3, 4 * node_label + 4
    else:
        if center.y <= search_point.y:
            return 1, 4 * node_label + 2
        else:
            return 2, 4 * node_label + 3


class NotFound(Exception):
    pass


class Tree(object):
    """Creates Class tree"""

    point_list = []
    triangle_list = []

    def __init__(self, d, c):
        self.root = Node(d)
        self.capacity = c

    def insert_list(self, points: list):
        """Inserts list of points"""
        self.point_list = points
        counter = 0
        for my_point in points:
            print("Inserting point: " + my_point.to_string)
            self.insert_point(self.root, 0, counter, my_point)
            counter += 1

            print()

    def insert_triangle_list(self, triangles: list):
        """Inserts triangles after points have already been added"""
        self.triangle_list = triangles
        counter = 0
        for my_triangle in triangles:
            print("Insert Triangle: " + str(counter) + " " + my_triangle.to_string)
            self.insert_triangle(counter, my_triangle)
            counter += 1
        print("")
        print("Preorder traversal: ")
        preorder(self.root, 0)
        print("END PR")

    def insert_triangle(self, triangle_index, my_triangle: Triangle):
        for my_point in my_triangle.all_points:
            loc, node_label = self.point_location(self.root, self.point_list[my_point], 0)
            loc.add_triangle(triangle_index, node_label)

    def insert_point(self, node: Node, node_label, point_index, p: Point):
        if node.has_children:
            self.insert_into_children(node, node_label, point_index, p)
        elif node.num_points_inside >= self.capacity:
            node.add_children(self.point_list)
            print("Adding children and sending points to leaves of node " + str(node_label))
            self.insert_point(node, node_label, point_index, p)
        else:
            print("Inserted point number " + str(point_index) + " into node " + str(node_label))
            node.add_point(point_index)

    def insert_into_children(self, node: Node, node_label, point_index, p: Point):
        center = node.center_point
        quad, new_node_label = quadrant_selector(center, p, node_label)
        self.insert_point(node.child(quad), new_node_label, point_index, p)

    def search_point_list(self, search_list: list):
        for my_point in search_list:
            print()
            print("Searching for point")
            if self.point_query(self.root, 0, my_point):
                print(my_point.to_string + "was found")
            else:
                print(my_point.to_string + "was not found")

    def point_query(self, node: Node, node_label, search_point: Point) -> bool:
        """Returns a boolean of whether the search_point is in the tree"""
        try:
            self.point_location(node, search_point, node_label)
            return True
        except NotFound:
            return False

    def point_location(self, node: Node, search_point: Point, node_label=0) -> (Node, int):
        """If the search_point is in the tree, returns the node and node_label, if not, raises NotFound Exception"""
        if node.has_children:
            center = node.center_point
            quad, new_node_label = quadrant_selector(center, search_point, node_label)
            return self.point_location(node.child(quad), search_point, new_node_label)
        elif node.point_in_node_list(search_point, self.point_list):
            return node, node_label
        else:
            raise NotFound("Couldn't find the point in the tree")

    def min_max_query(self):
        minima = set()
        maxima = set()
        vertex_neighbors = self.get_neighbors()
        for x in range(len(vertex_neighbors)):
            max_check, min_check = self.compare_to_neighbors(self.point_list[x], vertex_neighbors[x])
            if max_check:
                maxima.add(x)
            if min_check:
                minima.add(x)
        print("")
        print("Maxima: " + str(maxima))
        print("Minima: " + str(minima))

    def get_neighbors(self) -> list:
        """returns a list where each position represents a vertex, and in that position are a set of it's neighbors"""
        vertex_neighbors = []
        for x in range(len(self.point_list)):
            vertex_neighbors.append(set())
        for my_triangle in self.triangle_list:
            points = my_triangle.all_points  # List of points
            for x in range(3):
                my_point = points[x]
                neighbor_point = points[(x + 1) % 3]
                vertex_neighbors[my_point].add(neighbor_point)
                neighbor_point = points[(x + 2) % 3]
                vertex_neighbors[my_point].add(neighbor_point)
        return vertex_neighbors

    def compare_to_neighbors(self, inspect_point: Point, neighbors: frozenset) -> (bool, bool):
        max_check = True
        min_check = True
        for compare_point_index in neighbors:
            compare_point = self.point_list[compare_point_index]
            if max_check and not inspect_point.is_higher(compare_point):
                max_check = False
            if min_check and not inspect_point.is_lower(compare_point):
                min_check = False
        return max_check, min_check
