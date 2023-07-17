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
            print("node can't insert")
        else:
            newnode = Node(nodeValue)
            if position == 0:
                newnode.prev =None
                newnode.next = self.head
                self.head.prev = newnode
                self.head = newnode
            elif position == 1:
                newnode.next = None
                newnode.prev = self.tail
                self.tail.next = newnode
                self.tail = newnode
            else:
                tempnode = self.head 
                index =0
                while index < position - 1:
                    tempnode = tempnode.next
                    index +=1 
                newnode.next = tempnode.next
                newnode.prev = tempnode
                newnode.next.prev= newnode
                tempnode.next = newnode
    def traversDLL(self):
        if self.head is None:
            print("nothing to traverse")
        else:
            tempnode = self.head
            while tempnode:
                print (tempnode.value)
                tempnode = tempnode.next
    def reversetraversDLL(self):
        if self.head is None:
            print("nothing to traverse")
        else:
            tempnode = self.tail
            while tempnode:
                print (tempnode.value)
                tempnode = tempnode.prev
    def searchDLL(self,nodeval):
        if self.head is None:
            print("nothing to search")
        else:
            tempnode = self.head
            while tempnode:
                if tempnode.value == nodeval:
                   print(tempnode.value)
                tempnode = tempnode.next
            print("node doe not exist")
                
                           

Double_linked_list = Double_LinkedList()
Double_linked_list.createDLL(12)
Double_linked_list.insertNode(1,1)
Double_linked_list.insertNode(1,14)
Double_linked_list.insertNode(1,13)
Double_linked_list.insertNode(2,13)
Double_linked_list.traversDLL()
Double_linked_list.reversetraversDLL()
Double_linked_list.searchDLL(13)
print([node.value for node in Double_linked_list])

