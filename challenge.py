import math


def square_area(side):
    """Returns the area of a square"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return side**2


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return base * height


def triangle_area(base, height):
    """Returns the area of a triangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (base * height)/2


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (diagonal_1 * diagonal_2)/2


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return ((base_minor + base_major)*height)/2


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (perimeter * apothem)/2


def circumference_area(radius):
    """Returns the area of a circumference"""
    # You have to code here
    # REMEMBER: Tests first!!!
    # Use math.pi for π value
    area = math.pi * (radius**2)
    return round(area,2)

if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            # Initialize the needed values for the tests
            global side, base, height, diagonal_1, diagonal_2,base_minor, base_major, perimeter, apothem, radius
            side = 2
            base = 3
            height = 4
            diagonal_1 = 8
            diagonal_2 = 6
            base_minor = 20
            base_major = 40
            perimeter = 30
            apothem = 4
            radius = 5

        def test_square_area(self):
            # Make this test first...
            result = square_area(side)

            self.assertEqual(result, 4)

        def test_rectangle_area(self):
            # Make this test first...
            result = rectangle_area(base, height)

            self.assertEqual(result, 12)

        def test_triangle_area(self):
            # Make this test first...
            result = triangle_area(base , height)

            self.assertEqual(result, 6)

        def test_rhombus_area(self):
            # Make this test first...
            result = rhombus_area(diagonal_1, diagonal_2)

            self.assertEqual(result, 24)

        def test_trapezoid_area(self):
            # Make this test first...
            result = trapezoid_area(base_minor, base_major, height)

            self.assertEqual(result, 120)

        def test_regular_polygon_area(self):
            # Make this test first...
            result = regular_polygon_area(perimeter, apothem)

            self.assertEqual(result, 60)

        def test_circumference_area(self):
            # Make this test first...
            result = circumference_area(radius)

            self.assertEqual(result, 78.54)

        def tearDown(self):
            # Delete the needed values for the tests
            pass

    unittest.main()
