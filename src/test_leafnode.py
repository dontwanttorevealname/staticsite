import unittest

from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        # Assuming LeafNode is defined with all necessary attributes as outlined earlier.
        Leafnode = LeafNode("p", "This is a leaf node")
        html_output = Leafnode.to_html()  # Call the method to get the output
        print(html_output)  # This will print the expected HTML string

        Leafnode2 = LeafNode("p", "This is a leaf node")
        self.assertEqual(Leafnode, Leafnode2)

if __name__ == "__main__":
    unittest.main()