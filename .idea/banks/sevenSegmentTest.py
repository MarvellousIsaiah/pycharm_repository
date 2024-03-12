import unittest

class TestSevenSegmentDisplay(unittest.TestCase):

    def test_fill_a(self):
        display = [[0, 0, 0, 0] for _ in range(5)]
        fill_a(display)
        self.assertEqual(display[0], [1, 1, 1, 1])

    def test_fill_b(self):
        display = [[0, 0, 0, 0] for _ in range(5)]
        fill_b(display)
        self.assertEqual(display[0][3], 1)
        self.assertEqual(display[1][3], 1)
        self.assertEqual(display[2][3], 1)

    def test_fill_c(self):
        display = [[0, 0, 0, 0] for _ in range(5)]
        fill_c(display)
        self.assertEqual(display[2][3], 1)
        self.assertEqual(display[3][3], 1)
        self.assertEqual(display[4][3], 1)

    def test_fill_d(self):
        display = [[0, 0, 0, 0] for _ in range(5)]
        fill_d(display)
        self.assertEqual(display[4], [1, 1, 1, 1])

    def test_fill_e(self):
        display = [[0, 0, 0, 0] for _ in range(5)]
        fill_e(display)
        self.assertEqual(display[2][0], 1)
        self.assertEqual(display[3][0], 1)
        self.assertEqual(display[4][0], 1)

    def test_fill_f(self):
        display = [[0, 0, 0, 0] for _ in range(5)]
        fill_f(display)
        self.assertEqual(display[0][0], 1)
        self.assertEqual(display[1][0], 1)
        self.assertEqual(display[2][0], 1)

    def test_fill_g(self):
        display = [[0, 0, 0, 0] for _ in range(5)]
        fill_g(display)
        self.assertEqual(display[2], [1, 1, 1, 1])

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, mock_stdout):
        display = [[1, 0, 1, 0] for _ in range(5)]
        expected_output = "#     #     \n\n#     #     \n\n#     #     \n\n#     #     \n\n#     #     \n"
        display_output(display)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_input_value(self):
        display = [[0, 0, 0, 0] for _ in range(5)]
        input_value('101', display)
        expected_output = [
            [1, 0, 1, 0],
            [1, 1, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 1, 1],
            [1, 0, 1, 0]
        ]
        self.assertEqual(display, expected_output)

if __name__ == '__main__':
    unittest.main()
