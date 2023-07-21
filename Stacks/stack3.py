class Node:
    def __init__(self, value = None):
        self.next = next
        self.value = value

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        curNode= self.head
        while curNode:
            yield curNode
            curNode = curNode.next
        
class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False
    
    def push(self, Value):
        node = Node(Value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            return "there is not an element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    def peek(self):
        if self.isEmpty():
            return "there is no element in stack"
        else:
            nodevalue = self.LinkedList.head.value
            return nodevalue
    
    def delete(self):
        self.LinkedList.head = None

customstack = Stack()
customstack.push(12)
customstack.push(2)
customstack.push(13)
print(customstack.peek())
print(customstack)
print(customstack.isEmpty())  