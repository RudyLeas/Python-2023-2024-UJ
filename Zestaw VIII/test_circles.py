# test_circles.py

# Prawdopodobnie importujesz Point z osobnego modułu
from points import Point
from circles import Circle
import pytest
import math

def test_circle_creation():
    circle = Circle(0, 0, 1)
    assert circle.pt == Point(0, 0)
    assert circle.radius == 1

def test_circle_equality():
    circle1 = Circle(0, 0, 1)
    circle2 = Circle(0, 0, 1)
    assert circle1.__eq__(circle2) is True


def test_circle_inequality():
    circle1 = Circle(0, 0, 1)
    circle2 = Circle(0, 0, 2)
    assert circle1.__ne__(circle2) is True

def test_circle_area():
    circle = Circle(0, 0, 2)
    assert circle.area() == 4 * math.pi

def test_circle_move():
    circle = Circle(0, 0, 1)
    circle.move(1, 2)
    assert circle.pt == Point(1, 2)

def test_circle_cover():
    circle1 = Circle(0, 0, 1)
    circle2 = Circle(2, 0, 1)
    covered_circle = circle1.cover(circle2)
    assert covered_circle == Circle(1, 0, 2)

def test_circle_from_points():
    point1 = Point(0, 0)
    point2 = Point(3, 0)
    point3 = Point(0, 4)

    circle = Circle.from_points((point1, point2, point3))
    assert circle.pt == Point(1.5, 2)
    assert circle.radius == pytest.approx(2.5, rel=1e-2)

def test_circle_box():
    circle = Circle(1, 2, 3)
    assert circle.top == 5
    assert circle.left == -2
    assert circle.bottom == -1
    assert circle.right == 4
    assert circle.width == 6
    assert circle.height == 6
    assert circle.topleft == Point(-2, 5)
    assert circle.bottomleft == Point(-2, -1)
    assert circle.topright == Point(4, 5)
    assert circle.bottomright == Point(4, -1)
