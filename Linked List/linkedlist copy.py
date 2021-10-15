class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

  def __str__(self):
    return str(self.data)

class LinkedList:
  root = None
  size = 0

  ## INSTANCE METHODS __
  def __init__(self, data=None):
    if data is not None:
      self.root = Node(data)
      self.size = 1

  def __len__(self):
    return self.size

  def __str__(self):
    if self.is_empty():
      return "[]"

    current = self.root
    result = str(current)
    while current.next is not None:
      result += f' -> {str(current.next)}'
      current = current.next
      return str(f'[{result}]')

  
  def __iter__(self):
    current = self.root
    while current is not None:
      yield current
      current = current.next

    

  def is_empty(self):
    if self.root is None:
      return True
    return False
    
  def insert_in_front(self, data):
    node = Node(data)
    # if list is empty
    if self.is_empty():
      
      self.root = node
      self.size += 1
      return node
    
    # if list is not empty
    node.next = self.root
    self.root = node
    self.size +=1

  def remove_front(self):
    pass
    
  def insert_at_end(self, data):
    node = Node(data)

    if self.is_empty():
      
      self.root = node
      self.size += 1
      return node
    
    

    
  def remove_last(self):
    pass
    
  def insert_at_index(self, data, index=0):
    pass

  def remove_at_index(self, index=0):
    pass
      
