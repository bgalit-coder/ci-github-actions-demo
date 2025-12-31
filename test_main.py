import unittest
from io import StringIO
import sys

from main import print_name


class TestMain(unittest.TestCase):
    def test_print_name(self):
        captured_output = StringIO()
        sys.stdout = captured_output  

        print_name()

        sys.stdout = sys.__stdout__  

        self.assertEqual(captured_output.getvalue().strip(), "Galit")


if __name__ == "__main__":
    unittest.main()

