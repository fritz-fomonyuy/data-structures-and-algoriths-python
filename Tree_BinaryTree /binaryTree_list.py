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

newBT = BinaryTree(10)  
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.insertNode("tea"))
print(newBT.searchNode("Drinks"))