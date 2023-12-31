from points import Point
import math


class Circle:

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.pt.x}, {self.pt.y}, {self.radius})"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return math.pi * self.radius ** 2

    def move(self, x, y):
        if not (isinstance(x, (int, float)) or isinstance(y, (int, float))):
            raise ValueError("wspolrzedne nieliczbowe")
        else:
            self.pt.x += x
            self.pt.y += y

    def cover(self, other):
        bigger = max(self.radius, other.radius)
        distance = math.sqrt((self.pt.x - other.pt.x) ** 2 + (self.pt.y - other.pt.y) ** 2)
        new_radius = bigger + distance / 2
        new_x = (self.pt.x + other.pt.x) / 2
        new_y = (self.pt.y + other.pt.y) / 2
        return Circle(new_x, new_y, new_radius)

    @classmethod
    def from_points(cls, points):
        if len(points) != 3:
            raise ValueError("Oczekiwano trzech punktów")


        x1, y1 = points[0].x, points[0].y
        x2, y2 = points[1].x, points[1].y
        x3, y3 = points[2].x, points[2].y

        # Sprawdzenie, współliniowości
        if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
            raise ValueError("Punkty są współliniowe, nie można utworzyć okręgu")

        # Obliczenia dla środka okręgu (x, y)
        x = ((x1 ** 2 + y1 ** 2) * (y2 - y3) + (x2 ** 2 + y2 ** 2) * (y3 - y1) + (x3 ** 2 + y3 ** 2) * (y1 - y2)) / \
            (2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))

        y = ((x1 ** 2 + y1 ** 2) * (x3 - x2) + (x2 ** 2 + y2 ** 2) * (x1 - x3) + (x3 ** 2 + y3 ** 2) * (x2 - x1)) / \
            (2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))

        # Obliczenie promienia
        radius = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)

        return cls(x, y, radius)

    @property
    def top(self):
        return self.pt.y + self.radius

    @property
    def left(self):
        return self.pt.x - self.radius

    @property
    def bottom(self):
        return self.pt.y - self.radius

    @property
    def right(self):
        return self.pt.x + self.radius

    @property
    def width(self):
        return 2 * self.radius

    @property
    def height(self):
        return 2 * self.radius

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)
