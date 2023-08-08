import QueueLinkedList as queue
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
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
def levelOrderTraverdsal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("value existr")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("value is found")
        else:
            searchNode(rootNode.leftChilf, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print ("value exist")
        else:
            searchNode(rootNode.rightChild, nodeValue)

newBTS = BSTNode(None)
print(insertNode(newBTS, 100))
print(insertNode(newBTS, 90))
print(newBTS.data)
preOrderTraversal(newBTS)
postOrderTraversal(newBTS)
inOrderTraversal(newBTS)
levelOrderTraverdsal(newBTS)
searchNode(newBTS, 90)