class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.value = value
        self.tag = tag
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError("Not yet implemented.")
    def props_to_html(self):
        return str(self.props)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag== other.tag and
                self.children == other.children and self.value == other.value and self.props == other.props)
    
class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
           super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        elif self.tag == None:
            return self.value
        else:
            if not self.props == None:
                return "<" + str(self.tag) + " " + str(self.props) + ">" + str(self.value) + "</" + str(self.tag) + ">"
            else:
                return "<" + str(self.tag) + ">" + str(self.value) + "</" + str(self.tag) + ">"
    
    def __eq__(self, other):
        if not isinstance(other, LeafNode):
            return False
        return (self.tag == other.tag and
                self.value == other.value and self.props == other.props)
    
class ParentNode(HTMLNode):
    def __init__(self, tag = None, children = None, props = None):
        super().__init__(tag=tag, children=children, props=props)


    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag is required")
        elif self.children == None:
            raise ValueError("Children are required")
        else:
            newchildren = []
            for child in self.children:
                newchild = child.to_html()
                newchildren.append(newchild)
            result = "<" + str(self.tag) + ">" + str(newchildren) + "</" + str(self.tag) + ">"
            return result
    def __eq__(self, other):
        if not isinstance(other, ParentNode):
            return False
        return (self.tag == other.tag and
                self.children == other.children and self.props == other.props)