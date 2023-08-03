


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




    

def levelOtravers(rootN):
    if not rootN:
        return
    else:
        customqueue = queue.Queue()
        customqueue.enqueue(rootN)
        while not (customqueue.isEmpty()):
            root = customqueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customqueue.enqueue(root.value.leftChild)
                
            if (root.value.rightChild is not None):
                customqueue.enqueue(root.value.rightChild) 

def searchBT(rootNode,nodeValue):
    if not rootNode:
        return "binaryTree not found"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root =customQueue.dequeue()
            if root.value.data == nodeValue:
                return True
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
            return False                       
def insertBT_Node(rootNode,newNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Node has added sucessfuly"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.rightChild = newNode
                return "Node has added sucessfuly"

def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        
        deepestNode = root.value
        return deepestNode 
def deleteDeepestNode(rootNode,dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
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

def deleteNodeBT(rootNode , node):
    if not rootNode:
        return "binary tree not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "node has been deleted succesfully"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        
        return "failed to delete node"
def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "binary tree deleted succesfully"

#newNode = TreeNode("malt")
# print(insertBT_Node(newBT,newNode))
deepNode =getDeepestNode(newBT)
print(deepNode.data)
deleteDeepestNode(newBT,deepNode)
deleteNodeBT(newBT,"Cold")
deleteBT(newBT)
levelOtravers(newBT)




