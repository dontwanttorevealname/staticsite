import unittest

from main import *
import os

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        source_directory = '/Users/harrymoxon/staticsite/src'
        destination_directory = '/Users/harrymoxon/staticsite/public'
        copydirectory(source_directory, destination_directory)


if __name__ == "__main__":
    unittest.main()