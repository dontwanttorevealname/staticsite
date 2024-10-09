import unittest

from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from main import *

class TestBlock(unittest.TestCase):
    def test_eq(self):

        text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item   
"""

        markdown_to_blocks(text)
        


if __name__ == "__main__":
    unittest.main()
