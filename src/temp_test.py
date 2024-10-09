from main import *
from htmlnode import *
file = """
* This is the first list item in a list block
* This is a list item
* This is another list item
"""
parentnode = convert_to_node("ul", file)

output = parentnode.to_html()
print(output)