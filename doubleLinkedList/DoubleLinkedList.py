
class Node:
    def __init__(self, value=None):
        """
        Node class represents a node in the doubly linked list.

        Args:
        - value: The value to be stored in the node.
        """
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        """
        DoubleLinkedList class represents a doubly linked list.

        Attributes:
        - head: The head node of the linked list.
        - tail: The tail node of the linked list.
        """
        self.head = None
        self.tail = None

    def __iter__(self):
        """
        Iterates over the doubly linked list.

        Yields:
        - The next node in the linked list.
        """
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, nodeValue):
        """
        Creates a doubly linked list with a single node.

        Args:
        - nodeValue: The value of the node to be created.

        Returns:
        - A string indicating that the doubly linked list has been created successfully.
        """
        node = Node(nodeValue)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node
        return "Double linked list created successfully."

    def insertNode(self, position, nodeValue):
        """
        Inserts a new node at the specified position in the doubly linked list.

        Args:
        - position: The position at which the new node should be inserted.
        - nodeValue: The value of the node to be inserted.

        Returns:
        - None
        """
        if self.head is None:
            print("Cannot insert node. Doubly linked list is empty.")
        else:
            newnode = Node(nodeValue)
            if position == 0:
                newnode.prev = None
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
                index = 0
                while index < position - 1:
                    tempnode = tempnode.next
                    index += 1
                newnode.next = tempnode.next
                newnode.prev = tempnode
                newnode.next.prev = newnode
                tempnode.next = newnode

    def traverseDLL(self):
        """
        Traverses and prints the values of nodes in the doubly linked list.

        Returns:
        - None
        """
        if self.head is None:
            print("Nothing to traverse. Doubly linked list is empty.")
        else:
            tempnode = self.head
            while tempnode:
                print(tempnode.value)
                tempnode = tempnode.next

    def reverseTraverseDLL(self):
        """
        Traverses and prints the values of nodes in the doubly linked list in reverse order.

        Returns:
        - None
        """
        if self.head is None:
            print("Nothing to traverse. Doubly linked list is empty.")
        else:
            tempnode = self.tail
            while tempnode:
                print(tempnode.value)
                tempnode = tempnode.prev

    def searchDLL(self, nodeValue):
        """
        Searches for a node with the given value in the doubly linked list.

        Args:
        - nodeValue: The value to be searched.

        Returns:
        - None
        """
        if self.head is None:
            print("Nothing to search. Doubly linked list is empty.")
        else:
            tempnode = self.head
            while tempnode:
                if tempnode.value == nodeValue:
                    print(tempnode.value)
                    return
                tempnode = tempnode.next
            print("Node does not exist.")

    def deleteNode(self, location):
        """
        Deletes a node at the specified position in the doubly linked list.

        Args:
        - location: The position of the node to be deleted.

        Returns:
        - None
        """
        if self.head is None:
            print("There is no element to delete.")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                currentNode = self.head
                index = 0
                while index < location- 1:
                    currentNode = currentNode.next
                    index += 1
                currentNode.next = currentNode.next.next
                currentNode.next.prev = currentNode
            print("Node has been deleted successfully.")

    def deleteEntireDLL(self):
        """
        Deletes the entire doubly linked list.

        Returns:
        - None
        """
        if self.head is None:
            print("Doubly linked list does not exist.")
        else:
            tempnode = self.head
            while tempnode:
                tempnode.prev = None
                tempnode = tempnode.next
            self.head = None
            self.tail = None
            print("Entire doubly linked list has been deleted.")


# Usage example

double_linked_list = DoubleLinkedList()
double_linked_list.createDLL(12)
double_linked_list.insertNode(1, 1)
double_linked_list.insertNode(1, 14)
double_linked_list.insertNode(1, 13)
double_linked_list.insertNode(2, 13)
double_linked_list.traverseDLL()
double_linked_list.reverseTraverseDLL()
double_linked_list.searchDLL(3)
double_linked_list.deleteNode(1)
double_linked_list.deleteEntireDLL()
print([node.value for node in double_linked_list])


        