class Queue:
    def __init__(self):
        """
        Initializes a new instance of the Queue class.

        Returns:
            None

        Initializes an empty list to represent the queue.

        Example:
            >>> customQueue = Queue()
        """
        self.items = []

    def __str__(self):
        """
        Returns a string representation of the queue.

        Returns:
            str: A string representation of the queue.

        Converts the items in the queue to strings and joins them with spaces.

        Example:
            >>> print(customQueue)
            12 14
        """
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.

        Checks if the list representing the queue is empty.

        Example:
            >>> customQueue.isEmpty()
            False
        """
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, item):
        """
        Adds an item to the rear of the queue.

        Parameters:
            item: The item to be added to the queue.

        Returns:
            str: "item inserted successfully".

        Appends the item to the end of the list representing the queue.

        Example:
            >>> customQueue.enqueue(12)
            "item inserted successfully"
        """
        self.items.append(item)
        return "item inserted successfully"
    
    def dequeue(self):
        """
        Removes the item from the front of the queue.

        Returns:
            str: "item has been deleted successfully".

        Removes the last item from the list representing the queue.

        Example:
            >>> customQueue.dequeue()
            "item has been deleted successfully"
        """
        self.items.pop()
        return "item has been deleted successfully"
    
    def peek(self):
        """
        Returns the item at the front of the queue without removing it.

        Returns:
            Any: The item at the front of the queue if the queue is not empty.
                 "queue is empty" if the queue is empty.

        Returns the first item from the list representing the queue if the queue is not empty.
        Otherwise, returns the string "queue is empty".

        Example:
            >>> customQueue.peek()
            12
        """
        if self.items == []:
            return "queue is empty"
        else:
            return self.items[0]
    
    def delete(self):
        """
        Deletes the queue.

        Returns:
            None

        Sets the list representing the queue to None, effectively deleting the queue.

        Example:
            >>> customQueue.delete()
        """
        self.items = None

customQueue = Queue()
customQueue.enqueue(12)
customQueue.enqueue(14)
customQueue.dequeue()
print(customQueue.isEmpty())
print(customQueue.peek())
print(customQueue)
customQueue.delete() 