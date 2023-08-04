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
newBT = BinaryTree(3)  