from linkednode import LinkedNode

class LinkedStack:
    def __init__(self):
        self._top = None
        self._size = 0
        
    def push(self, value):
        self._top = LinkedNode(value, self._top)

        self._size += 1
            
    def __str__(self):
        if self._top is None:
            return 'LinkedStack([])'
        else:
            return 'LinkedStack([' + str(self._top) +'])'
        
    def pop(self):
        if (not self._top):
            raise ValueError('The stack is empty')
        oldTop = self._top
        self._top = oldTop.tail
        oldTop.tail = None
        self._size -= 1
        return oldTop.data
 
    def peek(self):
        if (not self._top):
            return None
        return self._top.data
    
    def __len__(self):
        return self._size
    
    def isempty(self):
        return len(self) == 0

stack = LinkedStack()
stack.push(3)
stack.push(4)
print(stack.pop())
print(stack.pop())
