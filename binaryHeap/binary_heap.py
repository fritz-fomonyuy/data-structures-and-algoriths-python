class Heap:
    def __init__(self,size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1
def peekOfHeap(rootNode):
    if not rootNode:
        return 
    else:
        return rootNode.customList[1]
def sizeOfHeap(rootNode):
    if not rootNode:
        return 
    else:
        return rootNode.heapSize
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1,rootNode.heapSize + 1):
            print(rootNode.customList[i])

def heapifyTreeInsert(rootNode,index, heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "min":
        if rootNode.customList[index]<rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex]=temp
        heapifyTreeInsert(rootNode,parentIndex,heapType)

    elif heapType == "max":
        if rootNode.customList[index]>rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex]=temp
        heapifyTreeInsert(rootNode,parentIndex,heapType)
def insertNode(rootNode,nodeValue, heapType):
    if rootNode.heapSize +1 == rootNode.maxSize:
        return "the binary tree is already full"
    rootNode.customList[rootNode.heapSize +1]= nodeValue
    rootNode.heapSize +=1
    heapifyTreeInsert(rootNode,rootNode.heapSize,heapType)
    return "the value has been successfully inserted" 


newHeap = Heap(5)
insertNode(newHeap,12,"min")
insertNode(newHeap,30,"min")
insertNode(newHeap,15,"min")
insertNode(newHeap,11,"min")
levelOrderTraversal(newHeap)