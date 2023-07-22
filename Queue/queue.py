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

        
customQueue = Queue()
customQueue.enqueue(12)
customQueue.enqueue(14)
print(customQueue.isEmpty())
print(customQueue)
    