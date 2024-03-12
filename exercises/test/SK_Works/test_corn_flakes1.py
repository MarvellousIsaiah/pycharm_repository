from unittest import TestCase
from exercises.SK_Works.corn_flakes1 import count_letters_and_digits


class Test(TestCase):
    def test_count_letters_and_digits(self):
        self.entry = "Hello World 123"
        expected = (10, 3)
        actual = count_letters_and_digits(self.entry)
        self.assertEqual(actual, expected)
