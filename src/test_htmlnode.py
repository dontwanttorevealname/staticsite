import unittest

from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        htmlnode = HTMLNode("This is a HTML node")
        htmlnode2 = HTMLNode("This is a HTML node")
        self.assertEqual(htmlnode, htmlnode2)

if __name__ == "__main__":
    unittest.main()