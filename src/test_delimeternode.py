import unittest

from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from main import text_node_to_html_node
from main import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a *text* node *donkey**dick*with *bold* words.", "text")
        new_nodes = split_nodes_delimiter([node], "*", "bold")




        newer_nodes = []
        for new_node in new_nodes:
            newer_node = text_node_to_html_node(new_node)
            evennewer_node = newer_node.to_html()
            newer_nodes.append(evennewer_node)
        output = "".join(newer_nodes)
        print(output)


if __name__ == "__main__":
    unittest.main()