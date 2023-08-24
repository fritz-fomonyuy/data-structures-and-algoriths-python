
class Stack:
    def __init__(self, maxSize):
        """
        Initializes a new instance of the Stack class.

        Parameters:
            maxSize (int): The maximum size of the stack.

        Returns:
            None

        Initializes the stack with the specified maximum size and an empty list.

        Example:
            >>> customStack = Stack(12)
        """
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        """
        Returns a string representation of the stack.

        Returns:
            str: A string representation of the stack.

        Reverses the list and joins its elements into a string, separated by newlines.

        Example:
            >>> print(customStack)
            2
        """
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.

        Checks if the list representing the stack is empty.

        Example:
            >>> customStack.isEmpty()
            True
        """
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        """
        Checks if the stack is full.

        Returns:
            bool: True if the stack is full, False otherwise.

        Checks if the length of the list representing the stack is equal to the maximum size.

        Example:
            >>> customStack.isFull()
            False
        """
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    def pop(self):
        """
        Removes and returns the top element of the stack.

        Returns:
            Any: The top element of the stack if the stack is not empty.
                 Otherwise, returns the string "the stack is full".

        Removes and returns the last element of the list representing the stack if the stack is not empty.
        Otherwise, returns the string "the stack is full".

        Example:
            >>> customStack.pop()
            2
        """
        if self.isEmpty:
            return "the stack is full"
        else:
            return self.list.pop()
    
    def push(self, value):
        """
        Adds an element to the top of the stack.

        Parameters:
            value: The value to be added to the stack.

        Returns:
            str: "the element has been successfully appended" if the stack is not full.
                 Otherwise, returns the string "stack is full".

        Adds the specified value to the end of the list representing the stack if the stack is not full.
        Otherwise, returns the string "stack is full".

        Example:
            >>> customStack.push(2)
            "the element has been successfully appended"
        """
        if self.isFull():
            return "stack is full"
        else:
            self.list.append(value)
            return "the element has been successfully appended"


customStack = Stack(12)
customStack.isFull()
print(customStack.isEmpty())
customStack.push(2)
customStack.push(2)
customStack.push(2)
print(customStack)