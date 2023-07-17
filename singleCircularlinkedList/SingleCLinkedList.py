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
                NewNode.next = nextNode
    
    def traversalSCLL(self):
        if self.head is None:
            return "SCLL is empty"
        else:
            temPnode = self.head
            while temPnode:
                print(temPnode.value)
                temPnode = temPnode.next
                if temPnode == self.tail.next:
                    break
    def SearchSCLl(self,nodeValue):
        if self.head is None:
            return "CSLL is empty"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode.next
                if tempNode == self.tail.next:
                    return "node doesnot exist in CSLL"
    def delete_Node_SCLL(self,position):
        if self.head is None:
            return "SCLL is empty"
        else:
            if position == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head =self.head.next
                    self.tail = self.head
            elif position == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < position - 1:
                    tempNode = tempNode.next
                    index +=1
                nextnode = tempNode.next
                tempNode.next =nextnode    


    def deleteEntireSCLL(self):
        self.head = None
        self.tail = None
                    

circularSll = single_circular_linked_list()
circularSll.creatSCLL(1)
circularSll.NodeInsertionSCLL(1,23)
circularSll.NodeInsertionSCLL(0,10)
circularSll.NodeInsertionSCLL(1,33)
print(circularSll.SearchSCLl(2))
circularSll.delete_Node_SCLL(1)
circularSll.deleteEntireSCLL()
print([node.value for node in circularSll])

