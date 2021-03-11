"""
Unit testing the calculator app
"""

import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        assert 5 == calculator.add(1, 4)

    def test_subtract(self):
        assert 2 == calculator.subtract(5, 3)

if __name__ == '__main__':
    unittest.main()
