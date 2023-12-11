from linkednode import LinkedNode

class LinkedQueue:
    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0
        
    def __str__(self):
        if self._front is None:
            return 'LinkedQueue([])'
        else:
            return 'LinkedQueue([' + str(self._front) +'])'

    def enqueue(self, value):
        linkedNode = LinkedNode(value)
        if (self._front):
            if (self._back is None): # 2 items
                self._front.tail = linkedNode
                self._back = linkedNode
            else: # more than 2 items
                oldBack = self._back
                self._back = linkedNode
                oldBack.tail = linkedNode
        else: # first item
            self._front = linkedNode
            self._front.tail = None
            
        self._size += 1
            
    def pop(self):
        if (not self._front):
            raise ValueError('The queue is empty')
        oldFront = self._front
        self._front = oldFront.tail
        oldFront.tail = None
        self._size -= 1    
        return oldFront.data
    
    def peek(self):
        if (not self._front):
            return None
        return self._front.data
    
    def __len__(self):
        return self._size
    
    def isempty(self):
        return len(self) == 0
            
queue = LinkedQueue()
queue.enqueue(5)
queue.enqueue(2)
queue.enqueue(13)
print(queue)
print(len(queue))
print(queue.isempty())
print(queue.pop())
print(queue)
print(queue.pop())
print(len(queue))
print(queue)
print(queue.peek())
print(queue.pop())
print(queue.isempty())