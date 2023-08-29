class BinaryTree:
    def __init__(self, size):
        """
        Initializes a binary tree object.

        Args:
            size (int): The size of the custom list representing the binary tree.
        """
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
        
    def insertNode(self, value):
        """
        Inserts a node with the given value into the binary tree.

        Args:
            value: The value to be inserted into the tree.

        Returns:
            str: A message indicating if the value has been successfully inserted or if the binary tree is full.
        """
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The binary tree is full"
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"

    def searchNode(self, nodeValue):
        """
        Searches for a node with the given value in the binary tree.

        Args:
            nodeValue: The value to search for in the tree.

        Returns:
            bool: True if the value is found, False otherwise.
        """
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return True
        return False

    def PreOrderTraversal(self, index):
        """
        Performs a pre-order traversal of the binary tree, starting from the specified index.

        Args:
            index (int): The starting index for the traversal.
        """
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.PreOrderTraversal(index * 2)
        self.PreOrderTraversal(index * 2 + 1)

    def inOrderTraversal(self, index):
        """
        Performs an in-order traversal of the binary tree, starting from the specified index.

        Args:
            index (int): The starting index for the traversal.
        """
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index * 2)
        print(self.customList[index])
        self.inOrderTraversal(index * 2 + 1)

    def postOrderTraversal(self, index):
        """
        Performs a post-order traversal of the binary tree, starting from the specified index.

        Args:
            index (int): The starting index for the traversal.
        """
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.customList[index])

    def levelOrderTraversal(self, index):
        """
        Performs a level-order traversal of the binary tree, starting from the specified index.

        Args:
            index (int): The starting index for the traversal.
        """
        for i in range(index, self.lastUsedIndex + 1):
            print(self.customList[i])

    def deleteNode(self, value):
        """
        Deletes a node with the given value from the binary tree.

        Args:
            value: The value to be deleted.

        Returns:
            str: A message indicating if the node has been successfully deleted or if the binary tree is empty.
        """
        if self.lastUsedIndex == 0:
            return "The binary tree is empty"
        for i in range(1, self.lastUsedIndex + 1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been deleted"

    def deleteBT(self):
        """
        Deletes the entire binary tree.

        Returns:
            str: A message indicating that the binary tree has been successfully deleted.
        """
        self.customList = None
        return "The binary tree has been successfully deleted"


# Example usage
newBT = BinaryTree(10)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.insertNode("tea"))
newBT.deleteNode("tea")
newBT.PreOrderTraversal(1)
newBT.postOrderTraversal(1)
newBT.inOrderTraversal(1)
newBT.levelOrderTraversal(1)
newBT.deleteBT()
