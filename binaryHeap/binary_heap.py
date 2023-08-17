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
def heapifyTreeExtract(rootNode,index,heapType):
    leftIndex = index * 2
    rightIndex = index * 2  + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "min":
            if rootNode.customList[index]> rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[leftIndex]
                rootNode.customList[leftIndex]=temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[leftIndex]
                rootNode.customList[leftIndex]=temp
            return
    else:
        if heapType == "max":
            if rootNode.customList[index]> rootNode.customList[rightIndex]:
               swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index]< rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[swapChild]
                rootNode.customList[swapChild]=temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                   swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index]< rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[swapChild]
                rootNode.customList[swapChild]=temp
    heapifyTreeExtract(rootNode,swapChild,heapType)
def extractNode(rootNode,heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1]= rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -=1
        heapifyTreeExtract(rootNode,1,heapType)
        return extractedNode
def deleteBHeap(rootNode):
    rootNode.customList = None
            
newHeap = Heap(5)
insertNode(newHeap,12,"min")
insertNode(newHeap,30,"min")
insertNode(newHeap,15,"min")
insertNode(newHeap,11,"min")
extractNode(newHeap,"min")
deleteBHeap(newHeap)
levelOrderTraversal(newHeap)
