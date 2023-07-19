class Node:     #class initializes the Nodes
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class Double_CircularLL: #class initialises head and tail references
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self): #function enhances printing the list as output
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def Creat_CLL(self,Node_Val): #function creats a node in a DCLL
        node = Node(Node_Val)
        self.head = node
        self.tail = node
        node.prev = node
        node.next = node

    def Insert_Node(self,Position,Node_value):
        if self.head == None:
            print("list not found")
        else:
            New_Node = Node(Node_value)
            if Position == 0:
                New_Node.prev = self.tail
                New_Node.next = self.head
                self.head.prev = New_Node 
                self.head = New_Node
                self.tail.next = self.head
            elif Position == 1:
                New_Node.next = self.head
                New_Node.prev = self.tail
                self.head.prev = New_Node
                self.tail.next = New_Node
                self.tail = New_Node
            else:
                Temp_Node = self.head
                index = 1
                while index < Position - 1:
                    Temp_Node = Temp_Node.next
                    index += 1
                New_Node.next = Temp_Node.next
                New_Node.prev = Temp_Node
                New_Node.next.prev = New_Node
                Temp_Node.next = New_Node
            return "the node has been inserted sucessfully"
Circular_DoubleLL = Double_CircularLL()
Circular_DoubleLL.Creat_CLL(45)
print([node.value for node in Circular_DoubleLL])




