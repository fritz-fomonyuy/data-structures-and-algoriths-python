import QueueLinkedList as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(rootNode):
    """
    Perform pre-order traversal of a binary tree (Root-Left-Right).
    Print the value of each node in the binary tree in pre-order sequence.
    """
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    """
    Perform in-order traversal of a binary tree (Left-Root-Right).
    Print the value of each node in the binary tree in in-order sequence.
    """
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    """
    Perform post-order traversal of a binary tree (Left-Right-Root).
    Print the value of each node in the binary tree in post-order sequence.
    """
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOtravers(rootN):
    """
    Perform level order traversal of a binary tree.
    Print the value of each node in the binary tree in level order sequence.
    """
    if not rootN:
        return
    else:
        customqueue = queue.Queue()
        customqueue.enqueue(rootN)
        while not customqueue.isEmpty():
            root = customqueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customqueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customqueue.enqueue(root.value.rightChild) 

def searchBT(rootNode, nodeValue):
    """
    Search for a node with a specific value in a binary tree.
    Returns True if the node is found, False otherwise.
    """
    if not rootNode:
        return "Binary tree not found"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return True
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return False

def insertBT_Node(rootNode, newNode):
    """
    Insert a new node into a binary tree.
    """
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Node has been added successfully"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.rightChild = newNode
                return "Node has been added successfully"

def getDeepestNode(rootNode):
    """
    Get the deepest node in a binary tree.
    Returns the deepest node in the binary tree.
    """
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode 

def deleteDeepestNode(rootNode, dNode):
    """
    Delete the deepest node in a binary tree.
    """
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.data == dNode:
                root.value = None
                return
            if root.value.leftChild:
                if root.value.leftChild == dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild:
                if root.value.rightChild == dNode:
                    root.value.rightChild = None
                    return
                else:
                   customQueue.enqueue(root.value.rightChild)

def deleteNodeBT(rootNode, node):
    """
    Delete a node with a specific value in a binary tree.
    """
    if not rootNode:
        return "Binary tree does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "Node has been deleted successfully"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Failed to delete node"

def deleteBT(rootNode):
    """
    Delete the entire binary tree.
    """
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "Binary tree deleted successfully"

# Test the functions
deepNode = getDeepestNode(newBT)
print(deepNode.data)
deleteDeepestNode(newBT, deepNode)
deleteNodeBT(newBT, "Cold")
deleteBT(newBT)
levelOtravers(newBT)