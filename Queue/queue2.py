class Queue1:
    def __init__(self, maxSize):
        """
        Initializes a new instance of the Queue1 class.

        Parameters:
            maxSize (int): The maximum size of the queue.

        Returns:
            None

        Initializes a list with maxSize number of None values to represent the queue.
        Sets the maximum size, start index, and top index of the queue.

        Example:
            >>> customQueue = Queue1(3)
        """
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        """
        Returns a string representation of the queue.

        Returns:
            str: A string representation of the queue.

        Converts the items in the queue to strings and joins them with spaces.

        Example:
            >>> print(customQueue)
            1 2 3
        """
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        """
        Checks if the queue is full.

        Returns:
            bool: True if the queue is full, False otherwise.

        Checks if the top index plus 1 is equal to the start index or if the start index is 0
        and the top index plus 1 is equal to the maximum size.

        Example:
            >>> customQueue.isFull()
            True
        """
        if self.top + 1 == self.start or (self.start == 0 and self.top + 1 == self.maxSize):
            return True
        else:
            return False

    def isEmpty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.

        Checks if the top index is -1.

        Example:
            >>> customQueue.isEmpty()
            False
        """
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        """
        Adds an element to the end of the queue.

        Parameters:
            value: The value to be added to the queue.

        Returns:
            str: "element inserted at the end of the queue" if the element is inserted successfully.
                 "queue is full" if the queue is already full.

        Inserts the value at the top index of the queue and updates the top index accordingly.
        If the top index reaches the maximum size, it wraps around to the start of the queue.
        If the start index is 0, it remains at 0.

        Example:
            >>> customQueue.enqueue(1)
            "element inserted at the end of the queue"
        """
        if self.isFull():
            return "queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "element inserted at the end of the queue"

    def dequeue(self):
        """
        Removes the element from the front of the queue.

        Returns:
            Any: The value of the element that is removed if the queue is not empty.
                 "queue is empty" if the queue is empty.

        Removes the element at the start index of the queue and updates the start index accordingly.
        If the start index reaches the maximum size, it wraps around to 0.
        If the start index becomes equal to the top index, it means the queue becomes empty and both indices are reset.

        Example:
            >>> customQueue.dequeue()
            1
        """
        if self.isEmpty():
            return "queue is empty"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement

    def peek(self):
        """
        Returns the value of the element at the front of the queue without removing it.

        Returns:
            Any: The value of the element at the front of the queue if the queue is not empty.
                 "empty queue" if the queue is empty.

        Returns the value of the element at the start index of the queue if the queue is not empty.
        Otherwise, returns the string "empty queue".

        Example:
            >>> customQueue.peek()
            2
        """
        if self.isEmpty():
            return "empty queue"
        else:
            return self.items[self.start]

    def delete(self):
        """
        Deletes the queue.

        Returns:
            None

        Resets the items list to contain maxSize number of Nonevalues, and resets the top and start indices to their initial values.

        Example:
            >>> customQueue.delete()
        """
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1

customQueue = Queue1(3)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.dequeue()
customQueue.peek()
customQueue.delete()
print(customQueue)