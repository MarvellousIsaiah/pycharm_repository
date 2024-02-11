import unittest
from exercises import calculator

class MyTestCase(unittest.TestCase):
    def test_that_two_numbers_can_add(self):
        answer = calculator.add(7,5)
        self.assertEqual(12,answer)


    def test_that_two_numbers_can_multiply(self):
        answer = calculator.multiply(7,5)
        self.assertEqual(35,answer)

    def test_that_two_number_can_sub(self):
            answer = calculator.sub(7,5)
            self.assertEqual(2,answer)



