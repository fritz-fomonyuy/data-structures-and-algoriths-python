class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode,NodeValue):
    if rootNode.data == None:
        rootNode.data = NodeValue
    elif NodeValue <= rootNode.data:
        if rootNode.leftChild == None:
            rootNode.leftChild = BSTNode(NodeValue)
        else:
            insertNode(rootNode.leftChild, NodeValue)
    else:
        if rootNode.rightChild == None:
            rootNode.rightChild = BSTNode(NodeValue)
        else:
            insertNode(rootNode.rightChild, NodeValue)
    return "node has been sucessfuly inserted"
newBTS = BSTNode(None)
print(insertNode(newBTS, 100))
