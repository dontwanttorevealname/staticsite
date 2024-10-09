import unittest

from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from main import text_to_textnodes

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        newtext = text_to_textnodes(text)
        print(newtext)  
if __name__ == "__main__":
    unittest.main()