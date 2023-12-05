import circles
import unittest
class TestCircleArea(unittest.TestCase):
    def setUp(self):
        self.circle1 = circles.Circle(1,1,2)
        self.circle2 = circles.Circle(2,2,3)
        self.circle3 = circles.Circle(3,3,4)
        self.circle4 = circles.Circle(3,3,4)
    def test_init(self):
        with self.assertRaises(ValueError):
            circles.Circle(0,1,-2)
    def test_repr(self):
        self.assertEqual(repr(self.circle1),"Circle(1, 1, 2)")
        self.assertEqual(repr(self.circle2),"Circle(2, 2, 3)")
        self.assertEqual(repr(self.circle3),"Circle(3, 3, 4)")
    def test__eq__(self):
        self.assertFalse(self.circle1.__eq__(self.circle2))
        self.assertTrue(self.circle3.__eq__(self.circle4))
    def test__ne__(self):
        self.assertTrue(self.circle1.__ne__(self.circle2))
        self.assertFalse(self.circle3.__ne__(self.circle4))
    def test_area(self):
        self.assertEqual(self.circle1.area(),12.566370614359172)
        self.assertEqual(self.circle2.area(),28.274333882308138)
        self.assertEqual(self.circle3.area(),50.26548245743669)
    def test_move(self):
        self.circle1.move(1,1)
        self.assertEqual(self.circle1.pt.x,2)
        self.assertEqual(self.circle1.pt.y,2)
        self.circle2.move(-1,-1)
        self.assertEqual(self.circle2.pt.x,1)
        self.assertEqual(self.circle2.pt.y,1)
        with self.assertRaises(ValueError):
            self.circle3.move('a','b')
    def test_cover(self):
        self.assertEqual(self.circle3.cover(self.circle4),circles.Circle(3.0,3.0,4.0))
