class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
            current.endOfString = True
            print("inserted successfully")
    def searchString(self, word):
            currentNode = self.root
            for i in word:
                node = currentNode.children.get(i)
                if node == None:
                    return False
                currentNode = node
            if currentNode.endOfString == True:
                return True
            else:
                return False 
def deleteString(root,word, index):
    ch = word[index]
    curentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(curentNode.children) > 1:
        deleteString(curentNode,word,index+1)
        return False
    if index == len(word) - 1:
        if len(curentNode.children)>= 1:
            curentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True
    if curentNode.endOfString == True:
        deleteString(curentNode,word, index + 1)
        return False
    canThisNodeBeDeleted = deleteString(curentNode,word,index + 1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False
newTrie = Trie()
newTrie.insertString("assnal")
newTrie.insertString("assgjjlijigjhlk")
newTrie.insertString("aswingd")
print(newTrie.searchString("fer"))
deleteString(newTrie.root,"assnal",0)
