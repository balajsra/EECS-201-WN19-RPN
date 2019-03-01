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


class TestKeys(unittest.TestCase):
    def test_percentage_1(self):
        result = rpn.calculate('72 5 %')
        self.assertEqual(3.6, result)
    
    def test_percentage_2(self):
        result = rpn.calculate('45 10.2 %')
        self.assertEqual(4.59, result)

    def test_exponent_1(self):
        result = rpn.calculate('2 4 ^')
        self.assertEqual(16, result)

    def test_exponent_2(self):
        result = rpn.calculate('5 3 ^')
        self.assertEqual(125, result)

    def test_int_div_1(self):
        result = rpn.calculate('11 4 //')
        self.assertEqual(2, result)

    def test_int_div_2(self):
        result = rpn.calculate('53 8 //')
        self.assertEqual(6, result)

    def test_fact_1(self):
        result = rpn.calculate('5 !')
        self.assertEqual(120, result)

    def test_fact_2(self):
        result = rpn.calculate('10 !')
        self.assertEqual(3628800, result)
    
    def test_bit_and_1(self):
        result = rpn.calculate('13 7 &')
        self.assertEqual(5, result)

    def test_bit_and_2(self):
        result = rpn.calculate('10 9 &')
        self.assertEqual(8, result)
    
    def test_bit_or_1(self):
        result = rpn.calculate('13 7 |')
        self.assertEqual(15, result)
    
    def test_bit_or_2(self):
        result = rpn.calculate('10 9 |')
        self.assertEqual(11, result)
    
    def test_bit_not_1(self):
        result = rpn.calculate('10 ~')
        self.assertEqual(-11, result)
    
    def test_bit_not_2(self):
        result = rpn.calculate('13 ~')
        self.assertEqual(-14, result)
