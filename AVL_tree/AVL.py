import QueueLinkedList as queue
class AVLNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1
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
def searchAVL(rootNode,nodeValue):
    if not rootNode.data == nodeValue:
        print("the value is found")
    elif nodeValue < rootNode.data :
        if rootNode.leftChild.data == nodeValue :
            print("found")
        else:
            searchAVL(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("found")
        else:
            searchAVL(rootNode.rightChild,nodeValue)

def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightRotation(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot
def leftRotation(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot
def getBalance(rootNode):
    if not rootNode:
        return
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotation(rootNode)
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotation(rootNode)
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode = rightRotation(rootNode.rightChild)
        return leftRotation(rootNode)
    return rootNode

def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)

def deleteNode(rootNode,nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild == None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild == None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild)>= 0:
        return rightRotation(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotation(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.rightChild = rightRotation(rootNode.leftChild)
        return rightRotation(rootNode)
    if balance < 1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rightRotation(rootNode.rightChild)
        return leftRotation(rootNode)
    return rootNode
def deleteAVL_Tree(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "avl tree has been deleted successfuly"   




newAVL = AVLNode(56)
newAVL = insertNode(newAVL,60)
newAVL = insertNode(newAVL, 39)
newAVL = deleteNode(newAVL, 56)
newAVL = deleteAVL_Tree(newAVL)
levelOrderTraverdsal(newAVL)