import unittest

from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from main import *

class TestBlock(unittest.TestCase):
    def test_eq(self):

        text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

## This is a sub-heading

* This is the first list item in a list block
* This is a list item
* This is another list item 

```
This is a code block
```

### This is another sub-heading

1. This is the first item in an ordered list.
2. This is the second item in an ordered list.
  
"""

        result = extract_title(text)
        print(result)
        


if __name__ == "__main__":
    unittest.main()
