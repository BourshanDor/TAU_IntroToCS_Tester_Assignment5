import math
import unittest
import hw5_315780122 as hw5
from hw5_315780122 import Point
from hw5_315780122 import Polygon
from hw5_315780122 import Linked_list
from hw5_315780122 import Node
from numpy import *
import numpy as np


def test_edges():
    isosceles_triangle1 = Polygon(Linked_list([Point(0, 0), Point(6, 0), Point(3, 3 ** 0.5 * 0.5 * 6)]))
    isosceles_triangle2 = Polygon(Linked_list([Point(0, 0), Point(3, 3 ** 0.5 * 0.5 * 6), Point(6, 0)]))
    isosceles_triangle3 = Polygon(Linked_list([Point(3, 3 ** 0.5 * 0.5 * 6), Point(0, 0), Point(6, 0)]))
    isosceles_triangle4 = Polygon(Linked_list([Point(3, 3 ** 0.5 * 0.5 * 6), Point(6, 0), Point(0, 0)]))
    angles = [60.0, 60.0, 60.0]
    np.testing.assert_almost_equal(angles, isosceles_triangle1.edges(), 1)
    np.testing.assert_almost_equal(angles, isosceles_triangle2.edges(), 1)
    np.testing.assert_almost_equal(angles, isosceles_triangle3.edges(), 1)
    np.testing.assert_almost_equal(angles, isosceles_triangle4.edges(), 1)

    square1 = Polygon(Linked_list([Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)]))
    square2 = Polygon(Linked_list([Point(1, 0), Point(1, 1), Point(0, 1), Point(0, 0)]))
    square3 = Polygon(Linked_list([Point(1, 1), Point(0, 1), Point(0, 0), Point(1, 0)]))
    square4 = Polygon(Linked_list([Point(0, 1), Point(0, 0), Point(1, 0), Point(1, 1)]))
    angles = [90.0, 90.0, 90.0, 90.0]
    np.testing.assert_almost_equal(angles, square1.edges(), 1)
    np.testing.assert_almost_equal(angles, square2.edges(), 1)
    np.testing.assert_almost_equal(angles, square3.edges(), 1)
    np.testing.assert_almost_equal(angles, square4.edges(), 1)

    pentagon1 = Polygon(
        Linked_list([Point(0, 0), Point(1, 0), Point(1, 1), Point(0.5, 3 ** 0.5 * 0.5 + 1), Point(0, 1)]))
    angles = [90.0, 90.0, 150.0, 60.0, 150.0]
    np.testing.assert_almost_equal(angles, pentagon1.edges(), 1)


class TestHw5(unittest.TestCase):
    def test_find_optimal_angle(self):
        trees = [Point(2, 1), Point(0, 3), Point(-1, 3), Point(-1, 1), Point(-1, -1), Point(0, -5)]
        self.assertAlmostEqual(1.570, hw5.find_optimal_angle(trees, 0.25 * math.pi), 2)

    def test_simple(self):
        square1 = Polygon(Linked_list([Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)]))
        square2 = Polygon(Linked_list([Point(0, 0), Point(1, 1), Point(0, 1), Point(1, 0)]))

        square3 = Polygon(Linked_list([Point(1, 1), Point(2, 2), Point(2, 0), Point(3, 1)]))

        pentagon1 = Polygon(Linked_list([Point(0, 0), Point(1, 1), Point(0, 1), Point(1, 0), Point(2, 0.5)]))
        self.assertEqual(True, square1.simple())
        self.assertEqual(False, square2.simple())
        self.assertEqual(False, square3.simple())
        self.assertEqual(False, pentagon1.simple())


