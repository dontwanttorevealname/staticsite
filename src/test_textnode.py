import unittest

from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()