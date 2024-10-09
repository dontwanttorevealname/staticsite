import unittest

from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from main import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):

        node = TextNode("This is a text node :) :) </b>", "text")
        node2 = TextNode("This is an image node", "image", "boot.dev/image")
        node3 = TextNode("This is an italic node", "bold")

        newnode = text_node_to_html_node(node)
        newnode2 = text_node_to_html_node(node2)
        newnode3 = text_node_to_html_node(node3)
        output = newnode.to_html()
        print(output)
        output = newnode2.to_html()
        print(output)
        output = newnode3.to_html()
        print(output)



if __name__ == "__main__":
    unittest.main()