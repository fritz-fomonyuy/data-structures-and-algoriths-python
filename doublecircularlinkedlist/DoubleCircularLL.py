class Node:
    """Class to represent a node in a double circular linked list."""
    
    def __init__(self, value):
        """
        Initialize a node object.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.next = None
        self.prev = None


class Double_CircularLL:
    """Class to represent a double circular linked list."""
    
    def __init__(self):
        """Initialize an empty double circular linked list."""
        self.head = None
        self.tail = None

    def __iter__(self):
        """
        Enhances printing the list as output using iterators.

        Yields:
            node: The nodes in the linked list.
        """
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def Creat_CLL(self, Node_Val):
        """
        Create a new node in the double circular linked list.

        Args:
            Node_Val: The value to be stored in the new node.
        """
        node = Node(Node_Val)
        self.head = node
        self.tail = node
        node.prev = node
        node.next = node

    def Insert_Node(self, Position, Node_value):
        """
        Insert a new node at the specified position in the linked list.

        Args:
            Position: The position at which the node should be inserted.
            Node_value: The value to be stored in the new node.

        Returns:
            str: A message indicating the success of the insertion.
        """
        if self.head == None:
            return "List not found"
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
            return "The node has been inserted successfully"

    def deleteNode(self, Position):
        """
        Delete a node from the specified position in the linked list.

        Args:
            Position: The position of the node to be deleted.

        Returns:
            str: A message indicating the success of the deletion.
        """
        if self.head is None:
            return "Linked list does not exist"
        else:
            if Position == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.next = None
                    self.tail.next = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.head.next = self.head
            elif Position == 1:
                if self.head == self.tail:
                    self.tail = None
                    self.head = None
                    self.tail.next = None
                    self.tail.prev = None
                else:
                    self.tail = self.tail.next
                    self.tail.next = self.tail
                    self.head.prev = self.head
            else:
                Temp_Node = self.head
                index = 0
                while index < Position - 1:
                    Temp_Node = Temp_Node.next
                    index += 1
                Temp_Node.next = Temp_Node.next.next
                Temp_Node.prev = Temp_Node.next.prev
                return "Node has been deleted successfully"

    def DeleteAll(self):
        """Delete all nodes in the linked list."""
        if self.head is None:
            print("Nothing to delete")
        else:
            self.tail.next = None
            tempnode = self.head
            while tempnode:
                tempnode.prev = None
                tempnode = tempnode.next
            self.head = None
            self.tail = None
            print("DLL has been deleted successfully")


# Example usage
Circular_DoubleLL = Double_CircularLL()
Circular_DoubleLL.Creat_CLL(45)
Circular_DoubleLL.Insert_Node(1, 4)
Circular_DoubleLL.deleteNode(1)
Circular_DoubleLL.DeleteAll()
print([node.value for node in Circular_DoubleLL])