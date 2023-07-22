class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self,item):
        self.items.append(item)
        return "item inserted sucessfullt"
    
    def dequeue(self):
        self.items.pop()
        return "item has been deleted sucessfully"
    def peek(self):
        if self.items == []:
            return "queue is empty"
        else:
            return self.items[0]
    def delete(self):
        self.items = None

        
customQueue = Queue()
customQueue.enqueue(12)
customQueue.enqueue(14)
customQueue.dequeue()
print(customQueue.isEmpty())
print(customQueue.peek())
print(customQueue)
customQueue.delete()  