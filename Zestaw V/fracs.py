from math import gcd
import unittest


def add_frac(frac1, frac2):
    numerator1, denominator1 = frac1
    numerator2, denominator2 = frac2
    numerator = numerator1 * denominator2 + numerator2 * denominator1
    denominator = denominator1 * denominator2
    divisor = gcd(numerator, denominator)
    return [numerator // divisor, denominator // divisor]


def sub_frac(frac1, frac2):
    numerator1, denominator1 = frac1
    numerator2, denominator2 = frac2
    numerator = numerator1 * denominator2 - numerator2 * denominator1
    denominator = denominator1 * denominator2
    divisor = gcd(numerator, denominator)
    return [numerator // divisor, denominator // divisor]


def mul_frac(frac1, frac2):
    numerator1, denominator1 = frac1
    numerator2, denominator2 = frac2
    numerator = numerator1 * numerator2
    denominator = denominator1 * denominator2
    divisor = gcd(numerator, denominator)
    return [numerator // divisor, denominator // divisor]


def div_frac(frac1, frac2):
    numerator1, denominator1 = frac1
    numerator2, denominator2 = frac2
    numerator = numerator1 * denominator2
    denominator = denominator1 * numerator2
    divisor = gcd(numerator, denominator)
    return [numerator // divisor, denominator // divisor]


def is_positive(frac):
    numerator, denominator = frac
    return numerator * denominator > 0


def is_zero(frac):
    numerator = frac[0]
    return numerator == 0


def cmp_frac(frac1, frac2):  # -1 | 0 | +1
    res = sub_frac(frac1, frac2)
    if res[0] > 0:
        return -1
    elif res[0] == 0:
        return 0
    else:
        return 1


def frac2float(frac):
    numerator, denominator = frac
    return numerator / denominator


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertFalse(is_positive([-1, 2]))
        self.assertFalse(is_positive([0, 2]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 1]))
        self.assertTrue(is_zero([0, 2]))
        self.assertFalse(is_zero([1, 2]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), -1)
        self.assertEqual(cmp_frac([1, 3], [1, 2]), 1)
        self.assertEqual(cmp_frac([2, 3], [4, 6]), 0)

    def test_frac2float(self):
        self.assertAlmostEqual(frac2float([1, 2]), 0.5)
        self.assertAlmostEqual(frac2float([3, 4]), 0.75)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
print(cmp_frac([1, 2], [1, 3]))
