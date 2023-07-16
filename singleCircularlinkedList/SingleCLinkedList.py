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
            node = node.next
            if node == self.head:
                break
            
    
    def creatSCLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "circular single linked list has been created"

    def NodeInsertionSCLL(self,position,nodevalue):
        if self.head is None:
             return "the head ref is empty"
        else:
            NewNode = Node(nodevalue)
            if position == 0:
               NewNode.next= self.head
               self.head = NewNode
               self.tail.next = NewNode
            elif position == 1:
                NewNode.next = self.tail.next
                self.tail.next = NewNode
                self.tail = NewNode
            else:
                tempNode = self.head
                index = 0
                while index < position - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = NewNode
                NewNode.next = tempNode
    



circularSll = single_circular_linked_list()
circularSll.creatSCLL(1)
circularSll.NodeInsertionSCLL(1,23)
print([node.value for node in circularSll])

