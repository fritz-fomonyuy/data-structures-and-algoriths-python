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


newHeap = Heap(5)