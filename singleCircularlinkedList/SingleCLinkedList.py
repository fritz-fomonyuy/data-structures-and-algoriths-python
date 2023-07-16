class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class single_circular_linked_list:
    def  __init__(self):
        self.head=None
        self.tail =None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
    
    def creatSCLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "circular single linked list has been created"
  
circularSll = single_circular_linked_list()
circularSll.creatSCLL(1)
