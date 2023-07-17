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
    def deletenode(self,location):
                if self.head is None:
                    print("there is no element to delete")
                else:
                    if location == 0:
                        if self.head == self.tail:
                            self.head = None
                            self.tail = None
                        else:
                            self.head =self.head.next
                            self.head.prev = None
                    elif location == 1:
                        if self.head ==self.tail:
                            self.head=None
                            self.tail = None
                        else:
                            self.tail = self.tail.prev
                            self.tail.next = None
                    else:
                        currentNode = self.head
                        index = 0
                        while index < location - 1:
                            currentNode = currentNode.next
                            index +=1
                        currentNode.next= currentNode.next.next
                        currentNode.next.prev = currentNode
                    print("node has been deleted succesfully")

    def deleteEntireDLL(self):
        if self.head== None:
            print("DLL not exist")
        else:
            self.head = None
            self.tail=None
            print("entire DLL has been deleted")


Double_linked_list = Double_LinkedList()
Double_linked_list.createDLL(12)
Double_linked_list.insertNode(1,1)
Double_linked_list.insertNode(1,14)
Double_linked_list.insertNode(1,13)
Double_linked_list.insertNode(2,13)
Double_linked_list.traversDLL()
Double_linked_list.reversetraversDLL()
Double_linked_list.searchDLL(3)
print([node.value for node in Double_linked_list])

