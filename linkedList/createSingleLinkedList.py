
class Node:
    """
    A class representing a node in a singly linked list.
    """

    def __init__(self, value=None):
        """
        Initialize a node object with a value.

        Args:
            value: The value to be stored in the node. Defaults to None.
        """
        self.value = value
        self.next = None


class SlinkedList:
    """
    A class representing a singly linked list.
    """

    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.head = None
        self.tail = None


singlelinkedList = SlinkedList()
node1 = Node(1)
node2 = Node(2)

singlelinkedList.head = node1
singlelinkedList.head.next = node2
singlelinkedList.tail = node2