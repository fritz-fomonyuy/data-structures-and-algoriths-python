class Node:
    def __init__(self, value=None):
        self.next = None
        self.value = value

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        """
        Allows iteration over the linked list nodes.

        Yields:
            Node: The next node in the linked list.

        Example:
            >>> for node in linkedList:
            ...     print(node.value)
            12
            2
            13
        """
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
        
class Stack:
    def __init__(self):
        self.linkedList = LinkedList()
    
    def __str__(self):
        """
        Returns a string representation of the stack.

        Returns:
            str: A string representation of the stack.

        Converts the values of each node in the linked list to strings and joins them with newlines.

        Example:
            >>> print(customstack)
            2
            12
        """
        values = [str(x.value) for x in self.linkedList]
        return '\n'.join(values)

    def isEmpty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.

        Checks if the head of the linked list is None.

        Example:
            >>> customstack.isEmpty()
            False
        """
        if self.linkedList.head is None:
            return True
        else:
            return False
    
    def push(self, value):
        """
        Adds an element to the top of the stack.

        Parameters:
            value: The value to be added to the stack.

        Returns:
            None

        Creates a new node with the specified value and inserts it at the head of the linked list.

        Example:
            >>> customstack.push(12)
        """
        node = Node(value)
        node.next = self.linkedList.head
        self.linkedList.head = node

    def pop(self):
        """
        Removes the top element from the stack.

        Returns:
            Any: The value of the top element if the stack is not empty.
                 "there is not an element in the stack" if the stack is empty.

        Removes the head node from the linked list and returns its value if the stack is not empty.
        Otherwise, returns the string "there is not an element in the stack".

        Example:
            >>> customstack.pop()
            12
        """
        if self.isEmpty():
            return "there is not an element in the stack"
        else:
            nodeValue = self.linkedList.head.value
            self.linkedList.head = self.linkedList.head.next
            return nodeValue

    def peek(self):
        """
        Returns the value of the top element without removing it.

        Returns:
            Any: The value of the top element if the stack is not empty.
                 "there is no element in stack" if the stack is empty.

        Returns the value of the head node in the linked list if the stack is not empty.
        Otherwise, returns the string "there is no element in stack".

        Example:
            >>> customstack.peek()
            2
        """
        if self.isEmpty():
            return "there is no element in stack"
        else:
            nodeValue = self.linkedList.head.value
            return nodeValue
    
    def delete(self):
        """
        Deletes the stack.

        Returns:
            None

        Sets the head of the linked list to None, effectively deleting the stack.

        Example:
            >>> customstack.delete()
        """
        self.linkedList.head = None

customstack = Stack()
customstack.push(12)
customstack.push(2)
customstack.push(13)
print(customstack.peek())
customstack.pop()
print(customstack)
print(customstack.isEmpty())