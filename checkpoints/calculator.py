##Patnox 27-07-2021

import sys
import ast

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "[x={},y={}]".format(self.x, self.y)

class Calculate:

        def str_get_closest(self, points):
            try:
                res = ast.literal_eval(points)
            except ValueError as ex:
                res = tuple()
            except SyntaxError as se:
                res = tuple()
            except:
                res = tuple()
            return self.get_closest(res)

        def get_distance(self, p1, p2):
            return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


        def get_closest(self, point_tuples):
            points = [Point(x, y) for (x, y) in point_tuples]
            min_dist, min_dist_pts = sys.maxsize, None
            for i in range(len(points) - 1):
                for j in range(i + 1, len(points)):
                    dist = self.get_distance(points[i], points[j])
                    if dist < min_dist:
                        min_dist = dist
                        min_dist_pts = ((points[i].x, points[i].y), (points[j].x, points[j].y))

            return min_dist_pts

