import unittest

from dyck_paths import bracket_combinations, bracket_combinations2


class TestCatalanNumbers(unittest.TestCase):
    def setUp(self):
        self.actual_input_output_set = (
            (0, 1), (1, 1), (2, 2), (3, 5), (4, 14), (5, 42), (6, 132), (7, 429), (8, 1430), (9, 4862), (10, 16796),
        )

    def test_dyck_paths_using_bracket_combinations(self):
        for actual_input, actual_output in self.actual_input_output_set:
            expected_output = bracket_combinations(actual_input)
            self.assertEqual(actual_output, expected_output)

    def test_dyck_paths_using_bracket_combinations2(self):
        for actual_input, actual_output in self.actual_input_output_set:
            expected_output = bracket_combinations2(actual_input)
            self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()
