import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add_1(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)

    def test_add_2(self):
        result = rpn.calculate('5 2 +')
        self.assertEqual(7, result)

    def test_sub_1(self):
        result = rpn.calculate('10 5 -')
        self.assertEqual(5, result)

    def test_sub_2(self):
        result = rpn.calculate('22 13 -')
        self.assertEqual(9, result)

    def test_mul_1(self):
        result = rpn.calculate('3 5 *')
        self.assertEqual(15, result)

    def test_mul_2(self):
        result = rpn.calculate('2 3 *')
        self.assertEqual(6, result)

    def test_div_1(self):
        result = rpn.calculate('28 7 /')
        self.assertEqual(4, result)

    def test_div_2(self):
        result = rpn.calculate('50 5 /')
        self.assertEqual(10, result)
