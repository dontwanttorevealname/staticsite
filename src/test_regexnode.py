import unittest

from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from main import extract_markdown_images
from main import extract_markdown_links

def result_expected(text, expected):
    if text == expected:
        return True
    else:
        print (str(text) + "not equal to" + str(expected))
        raise Exception ("Results not the same.")

class TestTextNode(unittest.TestCase):
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    end = extract_markdown_images(text)

    text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    end2 = extract_markdown_links(text2)
    expected = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
    expected2 = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]
    print(result_expected(end, expected), result_expected(end2, expected2))

        


if __name__ == "__main__":
    unittest.main()