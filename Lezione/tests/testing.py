import unittest

from ..lol.ripasso import Calc

class TestCalculations(unittest.TestCase):

    def setUp(self) -> None:
        self.calculation = Calc(8, 2)

    def test_sum(self):

        self.assertEqual(self.calculation.get_sum(), 10, "The sum is wrond")