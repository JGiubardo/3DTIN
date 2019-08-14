
import sys  # sys.stdout.write
from point import Point
from domain import Domain
from tree import Tree
from triangle import Triangle


def read_mesh_file(url_in):
    points = []
    triangles = []

    with open(url_in) as infile:
        length = infile.readline().strip()
        length = int(length)
        vertices_num = infile.readline().strip()
        vertices_num = int(vertices_num)
        for l in range(vertices_num):
            line = (infile.readline()).split()
            point = Point(int(line[0]), int(line[1]), int(line[2]))
            points.append(point)
        triangles_num = infile.readline().strip()
        triangles_num = int(triangles_num)
        for l in range(triangles_num):
            line = (infile.readline()).split()
            triangle = Triangle(int(line[0]), int(line[1]), int(line[2]))
            triangles.append(triangle)
        infile.close()
        return length, points, triangles


def get_point(x: int) -> Point:
    return insert_points[x]


if __name__ == '__main__':
    insert_file = sys.argv[1]
    capacity = int(sys.argv[2])
    size, insert_points, insert_triangles = read_mesh_file(insert_file)
    my_tree = Tree(Domain(size/2, size/2, size), capacity)
    my_tree.insert_list(insert_points)
    my_tree.insert_triangle_list(insert_triangles)
    my_tree.min_max_query()
