class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head == None
    def addFront(self, node):
        if self.isEmpty():
            self.head = node
            self.tail = self.head
        else:
            node.setNext(self.head)
            self.head = node
    def addRear(self, node):
        if self.isEmpty():
            self.tail = node
            self.head = self.tail
        else:
            self.tail.setNext(node)
            self.tail = node
    def show(self):
        current = self.head
        data = '' 
        while current != None:
            data += f'[ {current.getData()}, {current.getNext()} ] -> '
            current = current.getNext()
        print(f'{data}')
    def removeFront(self):
        if self.isEmpty():
            return None
        else:
            temp = self.head
            self.head = self.head.getNext()
            return temp
    def removeRear(self):
        if self.isEmpty():
            return None
        else:
            current = self.head
            previous = None
            while current.getNext() != None:
                previous = current
                current = current.getNext()
            previous.setNext(None)
            return current