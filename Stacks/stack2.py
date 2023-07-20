class Stack:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.list= []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty:
            return "the stack is full"
        else:
            return self.list.pop()
    
    def push(self,Value):
        if self.isFull():
            return "stack is full"
        else:
            self.list.append(Value)
            return "the element has been sucessfuly appended"


customStack = Stack(12)
customStack.isFull()
print(customStack.isEmpty())
customStack.push(2)
print(customStack)

