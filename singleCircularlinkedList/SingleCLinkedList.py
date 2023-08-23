
class Node:
    def __init__(self, value):
        """
        Node class represents a node in the circular linked list.

        Args:
        - value: The value to be stored in the node.
        """
        self.value = value
        self.next = None


class SingleCircularLinkedList:
    def __init__(self):
        """
        SingleCircularLinkedList class represents a circular linked list.

        Attributes:
        - head: The head node of the linked list.
        - tail: The tail node of the linked list.
        """
        self.head = None
        self.tail = None

    def __iter__(self):
        """
        Iterates over the circular linked list.

        Yields:
        - The next node in the linked list.
        """
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.head:
                break

    def createSCLL(self, nodeValue):
        """
        Creates a circular single linked list with a single node.

        Args:
        - nodeValue: The value of the node to be created.

        Returns:
        - A string indicating that the circular single linked list has been created.
        """
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "Circular single linked list has been created."

    def nodeInsertionSCLL(self, position, nodeValue):
        """
        Inserts a new node at the specified position in the circular linked list.

        Args:
        - position: The position at which the new node should be inserted.
        - nodeValue: The value of the node to be inserted.

        Returns:
        - None
        """
        if self.head is None:
            return "The head reference is empty."
        else:
            newNode = Node(nodeValue)
            if position == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif position == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < position - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def traversalSCLL(self):
        """
        Traverses and prints the values of nodes in the circular linked list.

        Returns:
        - None
        """
        if self.head is None:
            return "SCLL is empty."
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    def searchSCLL(self, nodeValue):
        """
        Searches for a node with the given value in the circular linked list.

        Args:
        - nodeValue: The value to be searched.

        Returns:
        - The value of the node if found, or a string indicating that the node does not exist in the circular linked list.
        """
        if self.head is None:
            return "CSLL is empty."
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "Node does not exist in CSLL."

    def deleteNodeSCLL(self, position):
        """
        Deletes a node at the specified position in the circular linked list.

        Args:
        - position: The position of the node to be deleted.

        Returns:
        - None
        """
        if self.head is None:
            return "SCLL is empty."
        else:
            if position == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
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
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    def deleteEntireSCLL(self):
        """
        Deletes all nodes in the circular linked list.

        Returns:
        - None
        """
        self.head = None
        self.tail = None


# Example usage of the SingleCircularLinkedList class
circularSll = SingleCircularLinkedList()
circularSll.createSCLL(1)
circularSll.nodeInsertionSCLL(1, 23)
circularSll.nodeInsertionSCLL(0, 10)
circularSll.nodeInsertionSCLL(1, 33)
print(circularSll.searchSCLL(2))
circularSll.deleteNodeSCLL(1)
circularSll.deleteEntireSCLL()
print([node.value for node in circularSll])