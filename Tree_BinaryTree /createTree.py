class TreeNode:
    def __init__(self, data, children=[]):
        """
        Initializes a TreeNode object.

        Args:
            data: The data value associated with the node.
            children: A list of child nodes (default is an empty list).
        """
        self.data = data
        self.children = children

    def __str__(self, level=0):
        """
        Returns a string representation of the tree rooted at the current node.

        Args:
            level: The level of the current node in the tree (default is 0).

        Returns:
            A string representing the tree structure with appropriate indentation.
        """
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 2)
        return ret

    def addChild(self, TreeNode):
        """
        Adds a child node to the current node.

        Args:
            TreeNode: The child node to add.
        """
        self.children.append(TreeNode)


# Create the tree structure
tree = TreeNode("Drinks", [])
cold = TreeNode("Cold", [])
hot = TreeNode("Hot", [])
tree.addChild(cold)
tree.addChild(hot)
tea = TreeNode("Tea", [])
coffee = TreeNode("Coffee", [])
cola = TreeNode("Cola", [])
fanta = TreeNode("Fanta", [])
cold.addChild(cola)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)

# Print the tree structure
print(tree)