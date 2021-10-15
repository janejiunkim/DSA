class Node():
    def __init__(self, data, next= None, prev= None):
        self.data = data
        self.next = next
        self.prev = prev

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, data):
        newNode = Node(data, None, self.head)

        if (not self.head):
            self.head = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail

        self.tail = newNode
    
    def dequeue(self):
        data = self.head.data
        self.head = self.head.next
        return data

    def isEmpty(self):
        return self.head == None
        
    def peek(self):
        if (isEmpty()):
            return 'empty list!'
        else:
            return self.head.data
