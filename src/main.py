from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
import re
import pdb
import os
import shutil
def main():
    pass

def text_node_to_html_node(text_node):
    if text_node.text_type.lower() == "text":
        return LeafNode(tag = None, value = text_node.text)
    elif text_node.text_type.lower() == "bold":
        return LeafNode(tag = "b", value = text_node.text)
    elif text_node.text_type.lower() == "italic":
        return LeafNode(tag = "i", value = text_node.text)
    elif text_node.text_type.lower() == "code":
        return LeafNode(tag = "code", value = text_node.text)
    elif text_node.text_type.lower() == "link":
        return LeafNode(tag = "a", value = text_node.text, props = {"href": text_node.url})
    elif text_node.text_type.lower() == "image":
        return LeafNode(tag = "img", value = "", props = [{"src": text_node.url}, {"alt": text_node.text}])
    else:
        raise Exception (str(text_node.text_type.lower()) + " is an invalid text type.")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        original_text_type = node.text_type
        parts = str(node.text).split(delimiter)
        new_values = [parts[i] for i in range(1, len(parts), 2)]
        for part in parts:
            for value in new_values:
                if part == value:
                    new_node = TextNode(part, text_type)
                    new_nodes.extend([new_node])
                    break
            else:
                new_node = TextNode(part, original_text_type)
                newnode = new_node
                new_nodes.extend([new_node])
    
  
    return new_nodes
                
def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return [(alt, url) for alt, url in matches]

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return [(anchor, url) for anchor, url in matches]

def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        original_text_type = node.text_type
        links = extract_markdown_links(node.text) # alt, url
        strings = split_and_tuple_links(node.text)
        for string in strings:
            if isinstance(string, tuple) and string in links:
                new_node = TextNode(string[0], "link", string[1])
                new_nodes.append(new_node)
            else:
                new_node = TextNode(string, original_text_type)
                new_nodes.append(new_node)
    return new_nodes

def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        original_text_type = node.text_type
        images = extract_markdown_images(node.text)
        strings = split_and_tuple_images(node.text)
        for string in strings:
            if isinstance(string, tuple) and string in images:
                new_node = TextNode(string[0], "image", string[1])
                new_nodes.append(new_node)
            else:
                new_node = TextNode(string, original_text_type)
                new_nodes.append(new_node)
    return new_nodes

def split_and_tuple_links(text):
    # Regular expression to match [text](url) patterns
    pattern = r'(\[[^\]]+\])(\([^)]+\))'
    # List to hold results
    result = []
    # Start index for searching
    start = 0
    # Find all matches
    for match in re.finditer(pattern, text):
        start_index, end_index = match.span() 
        # Add text before the match
        if start_index > start:
            result.append(text[start:start_index])
        # Extract and clean the matched parts
        text_part = match.group(1)[1:-1]  # Remove the surrounding brackets []
        url_part = match.group(2)[1:-1]   # Remove the surrounding parentheses ()
        # Add the cleaned tuple to the results
        result.append((text_part, url_part))
        # Update start index for next iteration
        start = end_index
    # Add any remaining text after the last match
    if start < len(text):
        result.append(text[start:])  
    return result


def split_and_tuple_images(text):
    pattern = r'(!\[[^\]]+\])(\([^)]+\))'
    result = []
    start = 0
    for match in re.finditer(pattern, text):
        start_index, end_index = match.span()
        if start_index > start:
            result.append(text[start:start_index])
        # Strip the leading '!' from the alt-text match group
        text_part = match.group(1)[2:-1]
        url_part = match.group(2)[1:-1]
        result.append((text_part, url_part))
        start = end_index
    if start < len(text):
        result.append(text[start:])
    return result

def text_to_textnodes(text):
    nodes = [TextNode(text, "text")]
    nodes = split_nodes_delimiter(nodes, "**", "bold")
    nodes = split_nodes_delimiter(nodes, "*", "italic")
    nodes = split_nodes_delimiter(nodes, "`", "code")
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_links(nodes)
    return nodes

def markdown_to_blocks(markdown):
    list = markdown.split("\n\n")
    newlist = []
    for item in list:
        if not item == "":
            trimmed_item = item.rstrip()
            newlist.append(trimmed_item)


    return(newlist)

def block_to_block_type(markdown):
    heading_pattern = re.compile(r'^#{1,6} .*')
    code_block_pattern = re.compile(r'^```\n[\s\S]*?\n```$', re.MULTILINE)
    quote_block_pattern = re.compile(r'^(> .*(\n|$))+', re.MULTILINE)
    unordered_list_pattern = re.compile(r'^([*-] .*(\n|$))+', re.MULTILINE)
    ordered_list_pattern = re.compile(r'^\d+\. .*', re.MULTILINE)

    if heading_pattern.match(markdown):
        return "heading"
    elif code_block_pattern.match(markdown):
        return "code"
    elif quote_block_pattern.match(markdown):
        return "quote"
    elif unordered_list_pattern.match(markdown):
        return "unordered_list"
    elif ordered_list_pattern.match(markdown):
        return "ordered_list"
    else:
        return "paragraph"

def block_to_plain_text(markdown):
    # Define patterns for different markdown elements
    heading_pattern = re.compile(r'^(#{1,6})\s+(.*)', re.MULTILINE)
    code_block_pattern = re.compile(r'^```\n([\s\S]*?)\n```$', re.MULTILINE)
    quote_block_pattern = re.compile(r'^> ?(.*)', re.MULTILINE)
    unordered_list_pattern = re.compile(r'^([*-])\s+(.*)', re.MULTILINE)
    ordered_list_pattern = re.compile(r'^(\d+)\.\s+(.*)', re.MULTILINE)

    # Process and strip markdown syntax
    # Strip heading markdown
    markdown = heading_pattern.sub(r'\2', markdown)
    # Strip code block markdown (but retain the code)
    markdown = code_block_pattern.sub(r'\1', markdown)
    # Strip quote markdown
    markdown = quote_block_pattern.sub(r'\1', markdown)
    # Strip unordered list markers
    markdown = unordered_list_pattern.sub(r'\2', markdown)
    # Strip ordered list numbers
    markdown = ordered_list_pattern.sub(r'\2', markdown)

    return markdown

def get_markdown_tag(tag, file):
    if tag == "heading":
        num = count_hashtags(file)
        return "h" + str(num)
    elif tag == "paragraph":
        return "p"
    elif tag == "quote":
        return "blockquote"
    elif tag == "code":
        return "code"
    elif tag == "unordered_list":
        return "ul"
    elif tag == "ordered_list":
        return "ol"
    else:
        return

def convert_to_node(tag, file):
    if tag == "code":
        subnode = LeafNode(tag, file)
        node = ParentNode("pre", [subnode])
    elif tag == "ul" or tag == "ol":
        subitems = file.split("\n")
        children = []
        for item in subitems:
            if not item == "":
                subnode = LeafNode("li", item)
                children.append(subnode)
        node = ParentNode(tag, children)
    else:
        node = LeafNode(tag, file)
    return node


def count_hashtags(heading):
    if not heading.startswith('#'):
        raise ValueError("The heading must start with a '#' character.")
    count = 0
    for char in heading:
        if char == '#':
            count += 1
        else:
            break
    if count < 1 or count > 6:
        raise ValueError("The number of leading '#' characters must be between 1 and 6.")
    return count


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    content = []
    for block in blocks:
        
        type = block_to_block_type(block)
        tag = get_markdown_tag(type, block)
        file = block_to_plain_text(block)
        node = convert_to_node(tag, file)
        result = node.to_html()
        content.append(node)
    endnode = ParentNode("div", content)
    return endnode


def copydirectory(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
        print(f"Removed existing directory '{dst}'")

    os.makedirs(dst)
    print(f"Made new directory '{dst}'")

    with os.scandir(src) as entries:
        for entry in entries:
            src_path = os.path.join(src, entry.name)
            dst_path = os.path.join(dst, entry.name)

            if entry.is_dir():
                print(f"Opening directory '{dst_path}'")
                copydirectory(src_path, dst_path)
            else:
                print(f"Copying file '{src_path}' to '{dst_path}'")
                shutil.copy2(src_path, dst_path)




main()