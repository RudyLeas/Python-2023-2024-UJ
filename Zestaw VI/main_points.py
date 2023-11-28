from points import Point
import unittest


class TestPoint(unittest.TestCase):
    def test_str(self):
        point = Point(1, 2)
        self.assertEqual(point.__str__(), "(1, 2)")

    def test_repr(self):
        point = Point(1, 2)
        self.assertEqual(point.__repr__(), "Point(1, 2)")

    def test_eq(self):
        point1 = Point(1, 2)
        point2 = Point(1, 2)
        point3 = Point(3, 4)
        self.assertTrue(point1.__eq__(point2))
        self.assertFalse(point1.__eq__(point3))

    def test_ne(self):
        point1 = Point(1, 2)
        point2 = Point(1, 2)
        point3 = Point(3, 4)
        self.assertFalse(point1.__ne__(point2))
        self.assertTrue(point1.__ne__(point3))

    def test_add(self):
        point1 = Point(1, 2)
        point2 = Point(3, 4)
        self.assertEqual(point1.__add__(point2), Point(4, 6))

    def test_sub(self):
        point1 = Point(1, 2)
        point2 = Point(3, 4)

        self.assertEqual(point1.__sub__(point2), Point(-2, -2))

    def test_mul(self):
        point1 = Point(1, 2)
        point2 = Point(3, 4)
        self.assertEqual(point1.__mul__(point2), 11)

    def test_cross(self):
        point1 = Point(1, 2)
        point2 = Point(3, 4)
        self.assertEqual(point1.cross(point2), -2)

    def test_length(self):
        point = Point(3, 4)

        self.assertEqual(point.length(), 5)

    def test_hash(self):
        point = Point(1, 2)
        self.assertEqual(point.__hash__(), hash((1, 2)))


if __name__ == "__main__":
    unittest.main()
