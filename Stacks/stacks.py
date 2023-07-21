''' --> stack implementation with list: unlimited size limit
        class Stack initializes the list: str function converts the stack items
        to strings and facilitates printing  '''
class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse
        values = [str(x) for x in self.list]
        return '\n'.join(values)

#checks if stack is empty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
# push an element to stack
    def push(self,value): 
        self.list.append(value)
        return "element inserted sucessfully"

#deletes the last element from the stack
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            self.list.pop()

#returns the last element without deleting   
    def peek(self):
        if self.isEmpty():
            return "True"
        else:
            return self.list[len(self.list)-1]

#delete the stack
    def delete(self):
        self.list = None
        
customStack = Stack()
customStack.push(2)
customStack.push(33)
customStack.pop()
print(customStack.peek())
print(customStack)

