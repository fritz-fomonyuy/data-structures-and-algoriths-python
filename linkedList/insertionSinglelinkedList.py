class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SlinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    #insertion

    def insertSLL(self, value ,location):
        newNode= Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location==1:
                newNode.next=None
                self.tail.next=newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode=tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next=newNode
                newNode.next = nextNode
    def traverseSLL(self):
        if self.head == None:
            print("list not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def searchinSLL(self, nodevalue):
        if self.head==None:
            return "SLLlist is empty"
        else:
            node = self.head
            while node is not None:
                if node.value == nodevalue:
                    return node.value
                node = node.next
            return "value doesnot exist in SLList"

    def deleteNode(self, location):
        if self.head ==None:
            return "SLL is empty"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode =tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    def deleteentireSLL(self):
        if self.head == None:
            return "list doesnot exist"
        else:
            self.head = None
            self.tail = None
            
singlelinkedList = SlinkedList()
singlelinkedList.insertSLL(1,1)
singlelinkedList.insertSLL(1,1)
singlelinkedList.insertSLL(2,2)
singlelinkedList.insertSLL(7,3)
print([node.value for node in singlelinkedList])

singlelinkedList.traverseSLL()
print(singlelinkedList.searchinSLL(3))
print(singlelinkedList.deleteNode(0))
singlelinkedList.traverseSLL()