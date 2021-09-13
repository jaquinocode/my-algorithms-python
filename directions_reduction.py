class DListNode:
  """
    A node in a doubly-linked list.
  """

  def __init__(self, data=None, prev=None, next=None):
    self.data = data
    self.prev = prev
    self.next = next

  def __repr__(self):
    return repr(self.data)


class DoublyLinkedList:

  def __init__(self):
    """
      Create a new doubly linked list.
      Takes O(1) time.
    """
    self.head = None
    self.tail = None

  def __repr__(self):
    """
      Return a string representation of the list.
      Takes O(n) time.
    """
    nodes = []
    curr = self.head
    while curr:
      nodes.append(repr(curr))
      curr = curr.next
    return '[' + ', '.join(nodes) + ']'

  def prepend(self, data):
    """
      Insert a new element at the beginning of the list.
      Takes O(1) time.
    """
    new_head = DListNode(data=data, next=self.head)
    if self.head:
      self.head.prev = new_head
      self.head = new_head
    elif self.head is None:
      self.head = new_head
      self.tail = new_head

  def append(self, data):
    """
      Insert a new element at the end of the list.
      Takes O(n) time.
    """
    new_tail = DListNode(data=data, prev=self.tail)
    if self.tail:
      self.tail.next = new_tail
      self.tail = new_tail
    elif self.tail is None:
      self.head = new_tail
      self.tail = new_tail

  def find(self, key):
    """
      Search for the first element with `data` matching
      `key`. Return the element or `None` if not found.
      Takes O(n) time.
    """
    curr = self.head
    while curr and curr.data != key:
      curr = curr.next
    return curr  # Will be None if not found

  def remove_elem(self, node):
    """
      Unlink an element from the list.
      Takes O(1) time.
    """
    if node.prev:
      node.prev.next = node.next
    if node.next:
      node.next.prev = node.prev
    if node is self.head:
      self.head = node.next
    if node is self.tail:
      self.tail = node.prev
    node.prev = None
    node.next = None

  def remove(self, key):
    """
      Remove the first occurrence of `key` in the list.
      Takes O(n) time.
    """
    elem = self.find(key)
    if not elem:
      return
    self.remove_elem(elem)

  def reverse(self):
    """
      Reverse the list in-place.
      Takes O(n) time.
    """
    self.tail = self.head
    curr = self.head
    prev_node = None
    while curr:
      prev_node = curr.prev
      curr.prev = curr.next
      curr.next = prev_node
      curr = curr.prev
    self.head = prev_node.prev

def reduce_directions(directions):
  north_south_directions = DoublyLinkedList()
  west_east_directions = DoublyLinkedList()

  for i in range(len(directions)):
    direction = directions[i]
    if 'NORTH' == direction == 'SOUTH':
      if direction == 'NORTH':

      elif direction == 'SOUTH':

    elif W or E:
      if direction = :

      elif E:
