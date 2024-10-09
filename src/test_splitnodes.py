import unittest


from main import split_nodes_links
from main import split_nodes_images
from textnode import TextNode

class TestSplitNode(unittest.TestCase):
    def test_eq(self):
        link_node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            "text",
        )
        image_node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", "text"
        )

        new_link_nodes = split_nodes_links([link_node])
        print("\n \n LINK NODES : \n \n")
        print(new_link_nodes)
        new_image_nodes = split_nodes_images([image_node])
        print("\n \n IMAGE NODES : \n \n")
        print(new_image_nodes)

if __name__ == "__main__":
    unittest.main()
