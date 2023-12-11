from linkednode import LinkedNode

class LinkedList:

    def __init__(self):
        self._front = None
        self._tail = None
        self._size = 0


    def __str__(self):
        if self._front is None:
            return 'LinkedList([])'
        else:
            return 'LinkedList([' + str(self._front) +'])'


    def __len__(self):
        """ 
        Rather than traversing the list from front to end, it is better to have an attribute _size
        that is updated every time we add or remove an element.
        The code below shows you how to traverse a linked list, from start to end. 
        To traverse the list, we need to use a local variable <currentnode> to move along the list, 
        we must not change/move the pointer _front.
            count = 0
            currentnode = self._front
            while currentnode is not None:
                count += 1
                currentnode = currentnode._next

        """        
        return self._size

    def append(self, value):
        newnode = LinkedNode(value)
        if self._front is None:
            self._front = newnode
            self._tail = newnode
        else:
            self._tail.tail = newnode
            self._tail = newnode

        self._size += 1

    def pop(self):
        if self == None:
            raise IndexError('The list is empty.')
        
        front_node = self._front
        self._front = self._front.tail
        front_node.tail = None
        self._size -= 1
        return front_node.data
    
    def clear(self):
        self._front = None
        self._tail = None
        self._size = 0
        
    def index(self, value, start = 0, stop = 2147483647):                
        currentNode = None
        for currentIndex in range(start, stop):
            if (currentNode == None):
                currentNode = self._front
            elif (currentNode.tail):
                currentNode = currentNode.tail
            else:
                break
            currentIndex += 1
            if (currentNode.data == value):
                return currentIndex - 1
        raise ValueError('Value is not present')
    
    def insert(self, index, object):
        objectNode = LinkedNode(object) # disgusting T-T
        if (index > len(self)):
            raise IndexError('Index is out of range')
        if (index == len(self)):
            self.append(object)
        else:
            beforeNode = self.getitem(index - 1)
            afterNode = self.getitem(index)
            
            if (index == 0):
                self._front = objectNode
                objectNode.tail = afterNode
            else:
                beforeNode.tail = objectNode
                objectNode.tail = afterNode
            
            self._size += 1
            
    def getitem(self, index):
        if (index >= len(self)):
            raise IndexError('Index is out of range')
        if (index == 0): # dirty hack
            return self._front
        currentNode = None
        for i in range(0, index + 1):
            if (currentNode == None):
                currentNode = self._front
            elif (currentNode.tail):
                currentNode = currentNode.tail
        return currentNode
        
    def __getitem__(self, index):
        return self.getitem(index).data
    
    def __setitem__(self, index, value):
        self.getitem(index).data = value

    def __contains__(self, value):
        try:
            self.index(value)
            return True
        except:
            return False
    
    def remove(self, value):
        if (len(self) > 1):
            currentNode = None
            afterNode = None
            for i in range(0, len(self)):
                if (currentNode == None):
                    currentNode = self._front
                elif (currentNode.tail):
                    currentNode = currentNode.tail
                    beforeNode = self.getitem(i - 1)
                if (i < len(self) - 1):
                    afterNode = self.getitem(i + 1)
                else:
                    afterNode = None
                
                if (currentNode.data == value):
                    if (i == 0):
                        self._front = afterNode
                    elif (i < len(self) - 1):
                        beforeNode.tail = afterNode
                    else:
                        beforeNode.tail = None
                    self._size -= 1
                    return

            raise ValueError('Item not present')
        else:
            raise IndexError('List is empty')
            
        

testList = LinkedList()

# testList.append('5')
# testList.append('3')
# testList.append('1')
# testList.append('2')
# print(testList.pop())
# print(testList)
# print(testList._front)

# testList.clear()
# testList.append('2')
# testList.append('234')
# testList.append('321')
# testList.append('34')
# testList.append('1235')
# testList.append('52343')
# testList.append('132')

# print(testList.index('52343'))

# testList.clear()
# testList.append('a')
# testList.append('b')
# testList.append('c')
# testList.append('e')
# testList.insert(2, 'd')
# testList.insert(0, 'z')
# print(testList)

testList.append('4')
testList.append('5')
testList.append('3')
testList.insert(0, '1')
print(testList)
testList.insert(4, '2')
print(testList)
testList.insert(3, '6')
print(testList)

testList.remove('2')

print(testList)

print('3' in testList)
print('2' in testList)