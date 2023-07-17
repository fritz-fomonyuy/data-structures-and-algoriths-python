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
    
    def insertNode(self,position,nodeValue):
        if self.head is None:
            return "node can't insert"
        else:
            node = Node(nodeValue)
            if position == 0:
                node.prev =None
                node.next = self.head
                self.head.prev = node
                self.head = node
            elif position == 1:
                node.next = None
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
            else:
                tempnode = self.head 
                index =0
                while index < position - 1:
                    tempnode = tempnode.next
                    index +=1 
                node.next = tempnode.next
                node.prev = tempnode
                node.next.prev= node
                tempnode.next = node
           
Double_linked_list = Double_LinkedList()
Double_linked_list.createDLL(12)
Double_linked_list.insertNode(1,1)
print([node.value for node in Double_linked_list])

