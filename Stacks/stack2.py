class Stack:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.list= []

    def __str__(self):
        values = self.list.reverse
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    