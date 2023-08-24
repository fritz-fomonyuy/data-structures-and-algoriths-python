class Stack:
    def __init__(self):
        """
        Initializes a new instance of the Stack class.

        Returns:
            None

        Initializes an empty list to represent the stack.

        Example:
            >>> customStack = Stack()
        """
        self.list = []

    def __str__(self):
        """
        Returns a string representation of the stack.

        Returns:
            str: A string representation of the stack.

        Reverses the list and joins its elements into a string, separated by newlines.

        Example:
            >>> print(customStack)
            33
            2
        """
        values = self.list.reverse
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

    def push(self, value):
        """
        Adds an element to the top of the stack.

        Parameters:
            value: The value to be added to the stack.

        Returns:
            str: "element inserted successfully".

        Adds the specified value to the end of the list representing the stack.

        Example:
            >>> customStack.push(2)
            "element inserted successfully"
        """
        self.list.append(value)
        return "element inserted successfully"

    def pop(self):
        """
        Removes the top element from the stack.

        Returns:
            str: "stack is empty" if the stack is empty.

        Removes the last element from the list representing the stack if the stack is not empty.

        Example:
            >>> customStack.pop()
            "stack is empty"
        """
        if self.isEmpty():
            return "stack is empty"
        else:
            self.list.pop()

    def peek(self):
        """
        Returns the top element of the stack without removing it.

        Returns:
            Any: The top element of the stack if the stack is not empty.
                 "True" if the stack is empty.

        Returns the last element from the list representing the stack if the stack is not empty.
        Otherwise, returns the string "True" indicating that the stack is empty.

        Example:
            >>> customStack.peek()
            2
        """
        if self.isEmpty():
            return "True"
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        """
        Deletes the stack.

        Returns:
            None

        Sets the list representing the stack to None, effectively deleting the stack.

        Example:
            >>> customStack.delete()
        """
        self.list = None

customStack = Stack()
customStack.push(2)
customStack.push(33)
customStack.pop()
print(customStack.peek())
print(customStack)