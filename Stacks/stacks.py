# Stacks in python
# implemented with a linked list
class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = None


class Stack():
    def __init__(self):
        self.head = None

    def push(self, data):
        self.head = Node(data, self.head)
    
    def pop(self):
        data = self.head.data
        self.head = self.head.next
        return data

    def peek(self):
        return self.head.data

    def isEmpty(self):
        return self.head == None
    

