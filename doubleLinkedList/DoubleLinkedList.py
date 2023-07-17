class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
        self.prev = None

class Double_LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node=node.next
    def createDLL(self,nodeValue):
      node = Node(nodeValue)
      node.next = None
      node.prev = None
      self.head = node
      self.tail=node
      return "Double linked list created sucessfully"

Double_linked_list = Double_LinkedList()
Double_linked_list.createDLL(12)
print([node.value for node in Double_linked_list])

