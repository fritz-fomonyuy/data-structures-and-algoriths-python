class BinaryTree:
    def __init__(self,size):
      self.customList = size * [None]
      self.lastUsedIndex = 0
      self.maxSize = size
    
    def insertNode(self,value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "the binarytree is full"
        self.customList[self.lastUsedIndex+1]=value
        self.lastUsedIndex += 1
        return "the value has been successfuly inserted"
    
    def searchNode(self,nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i]== nodeValue:
                return True
        return False
    
    def PreOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.PreOrderTraversal(index * 2)
        self.PreOrderTraversal(index * 2 + 1)
    
    def inOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2 + 1)    

    def postOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2 + 1)
        print(self.customList[index])

    def levelOrderTraversal(self, index):
        for i in range(index,self.lastUsedIndex +1):
            print(self.customList[i])

    def deleteNode(self,value):
        if self.lastUsedIndex == 0:
            return "BT is empty"
        for i in range(1,self.lastUsedIndex+1 ):
            if self.customList[i]== value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex]=None
                self.lastUsedIndex -= 1
                return "the node has been deleted"

    def deleteBT(self):
        self.customList = None
        return "the binary tree has been successfuly deleted"

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
