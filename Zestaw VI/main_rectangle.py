from points import Point
from rectangle import Rectangle

import unittest

class TestRectangle(unittest.TestCase):
    def test_str(self):
        rectangle = Rectangle(1, 2, 3, 4)
        self.assertEqual(rectangle.__str__(), "[(1, 2), (3, 4)]")

    def test_repr(self):
        rectangle = Rectangle(1, 2, 3, 4)
        self.assertEqual(rectangle.__repr__(), "Rectangle(1, 2, 3, 4)")

    def test_eq(self):
        rectangle1 = Rectangle(1, 2, 3, 4)
        rectangle2 = Rectangle(1, 2, 3, 4)
        rectangle3 = Rectangle(5, 6, 7, 8)
        self.assertTrue(rectangle1.__eq__(rectangle2))
        self.assertFalse(rectangle1.__eq__(rectangle3))

    def test_ne(self):
        rectangle1 = Rectangle(1, 2, 3, 4)
        rectangle2 = Rectangle(1, 2, 3, 4)
        rectangle3 = Rectangle(5, 6, 7, 8)
        self.assertFalse(rectangle1.__ne__(rectangle2))
        self.assertTrue(rectangle1.__ne__(rectangle3))

    def test_center(self):
        rectangle = Rectangle(1, 2, 5, 6)
        result = rectangle.center()
        self.assertEqual(result, Point(3.0, 4.0))

    def test_area(self):
        rectangle = Rectangle(1, 2, 5, 6)
        result = rectangle.area()
        self.assertEqual(result, 16)

    def test_move(self):
        rectangle = Rectangle(1, 2, 3, 4)
        rectangle.move(1, 1)
        self.assertEqual(rectangle.pt1, Point(2, 3))
        self.assertEqual(rectangle.pt2, Point(4, 5))

if __name__ == "__main__":
    unittest.main()
