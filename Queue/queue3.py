class Node:
    """
    Represents a node in a linked list.
    """

    def __init__(self, value=None):
        """
        Initializes a new node with the given value.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.next = None

    def __str__(self):
        """
        Returns a string representation of the node's value.

        Returns:
            A string representation of the node's value.
        """
        return str(self.value)


class LinkedList:
    """
    Represents a linked list.
    """

    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None
        self.tail = None

    def __iter__(self):
        """
        Iterates over the nodes in the linked list.

        Yields:
            Each node in the linked list.
        """
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Queue:
    """
    Represents a queue implemented using a linked list.
    """

    def __init__(self):
        """
        Initializes an empty queue.
        """
        self.linkedList = LinkedList()

    def __str__(self):
        """
        Returns a string representation of the queue.

        Returns:
            A string representation of the queue.
        """
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    def enqueue(self, value):
        """
        Adds an element to the end of the queue.

        Args:
            value: The value to be enqueued.
        """
        newNode = Node(value)
        if self.linkedList.head is None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    def isEmpty(self):
        """
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        if self.linkedList.head is None:
            return True
        else:
            return False

    def dequeue(self):
        """
        Removes and returns the element at the front of the queue.

        Returns:
            The element at the front of the queue.
        """
        if self.isEmpty():
            return "There is no node in the queue"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode

    def peek(self):
        """
        Returns the element at the front of the queue without removing it.

        Returns:
            The element at the front of the queue.
        """
        if self.isEmpty():
            return "Empty queue"
        else:
            return self.linkedList.head
customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.isEmpty())
customQueue.dequeue()
print(customQueue.peek())
print(customQueue)