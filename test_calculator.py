import unittest
from unittest.mock import patch
import tempfile
from calculator import (
    validate_file,
    collect_numbers,
    add_numbers,
    floats_to_strings,
    write_results_to_file
)


class ValidateFileTests(unittest.TestCase):

    @patch("os.path.exists", return_value=True)
    @patch("os.access", return_value=True)
    def test_validate_file_existing_readable_file(
            self, mock_access, mock_path_exists):
        input_file = "existing_readable_file.txt"

        result = validate_file(input_file)

        self.assertTrue(result)

    @patch("os.path.exists", return_value=False)
    def test_validate_file_nonexistent_file(self, mock_path_exists):
        input_file = "nonexistent_file.txt"

        with self.assertRaises(FileNotFoundError):
            validate_file(input_file)


class CollectNumbersTests(unittest.TestCase):

    @unittest.mock.patch("builtins.open", unittest.mock.mock_open(
        read_data="1.0\n2.0\n3.0\n4.0\n"))
    def test_collect_numbers(self):
        numbers = collect_numbers("numbers.txt")

        self.assertEqual(numbers, [1.0, 2.0, 3.0, 4.0])

    @unittest.mock.patch("builtins.open", unittest.mock.mock_open(
        read_data=""))
    def test_collect_numbers_empty_file(self):
        numbers = collect_numbers("numbers.txt")

        self.assertEqual(numbers, [])


class AddNumbersTests(unittest.TestCase):

    def test_add_numbers_empty_list(self):
        numbers = []

        results = add_numbers(numbers)

        self.assertEqual(results, [])

    def test_add_numbers_one_number(self):
        numbers = [1]

        results = add_numbers(numbers)

        self.assertEqual(results, [])

    def test_add_numbers_two_numbers(self):
        numbers = [1, 2]

        results = add_numbers(numbers)

        self.assertEqual(results, [3])

    def test_add_numbers_multiple_numbers(self):
        numbers = [1, 2, 3, 4]

        results = add_numbers(numbers)

        self.assertEqual(results, [3, 7])

    def test_add_numbers_negative_numbers(self):
        numbers = [-1, -2]

        results = add_numbers(numbers)

        self.assertEqual(results, [-3])

    def test_add_numbers_mixed_numbers(self):
        numbers = [1, -2, 3, -4]

        results = add_numbers(numbers)

        self.assertEqual(results, [-1, -1])


class FloatsToStringsTest(unittest.TestCase):

    def test_floats_to_strings_empty_list(self):
        results = []

        string_list = floats_to_strings(results)

        self.assertEqual(string_list, [])

    def test_floats_to_strings_one_number(self):
        results = [1.0]

        string_list = floats_to_strings(results)

        self.assertEqual(string_list, ["1.0"])

    def test_floats_to_strings_multiple_numbers(self):
        results = [1.0, 2.0, 3.0, 4.0]

        string_list = floats_to_strings(results)

        self.assertEqual(string_list, ["1.0", "2.0", "3.0", "4.0"])

    def test_floats_to_strings_negative_numbers(self):
        results = [-1.0, -2.0, -3.0, -4.0]

        string_list = floats_to_strings(results)

        self.assertEqual(string_list, ["-1.0", "-2.0", "-3.0", "-4.0"])

    def test_floats_to_strings_mixed_numbers(self):
        results = [1.0, -2.0, 3.0, -4.0]

        string_list = floats_to_strings(results)

        self.assertEqual(string_list, ["1.0", "-2.0", "3.0", "-4.0"])


class WriteResultsTest(unittest.TestCase):
    def test_write_results_to_file(self):

        string_list = ["This is the first line.", "This is the second line."]

        with tempfile.NamedTemporaryFile(mode='w') as output_file:
            write_results_to_file(output_file.name, string_list)

            with open(output_file.name, "r") as file:
                actual_output = file.read()

        expected_output = "This is the first line.\nThis is the second line.\n"

        self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()
