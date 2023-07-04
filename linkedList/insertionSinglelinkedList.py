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
                self.head


singlelinkedList = SlinkedList()
node1=Node(1)
node2=Node(2)

singlelinkedList.head =node1
singlelinkedList.head.next=node2
singlelinkedList.tail=node2
