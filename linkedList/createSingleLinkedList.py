class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SlinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

singlelinkedList = SlinkedList()
node1=Node(1)
node2=Node(2)

singlelinkedList.head =node1
singlelinkedList.head.next=node2
singlelinkedList.tail=node2
