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

# from timeit import default_timer as timer
#
# ll = DoublyLinkedList()
# ll.append(25)
# ll.append(58)
# ll.append(93)
# ll.append('hello')
# ll.append(282)
# print(f'll: {ll}')

# ll2 = DoublyLinkedList()
# ll2.append(8)
# ll2.append(16)
# ll2.append('howdydo')
# ll2.append(32)
# print(f'll2: {ll2}')

# # connect both ll's and set heads and tails to final connected ll
# # start here
# start = timer()
# ll.tail.next = ll2.head
# ll2.head.prev = ll.tail
# ll.tail = ll2.tail
# ll2.head = ll.head
# end = timer()
# # end here
# print(f'end - start: {end - start}')
# print(f'new ll: {ll}')
# print(f'new ll2: {ll2}')

# # ll library test
# # setup
# from llist import dllist, dllistnode
# import random

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# for i in range(5000):
#   r = random.randint(1, 100000)
#   list1.append(r)
#   r = random.randint(1, 100000)
#   list2.append(r)

# llist1 = dllist([1, 2, 3])
# llist2 = dllist([4, 5, 6])
# for i in range(5000):
#   r = random.randint(1, 100000)
#   llist1.append(r)
#   r = random.randint(1, 100000)
#   llist2.append(r)
# # end setup

# start2 = timer()
# llist3 = llist1 + llist2
# end2 = timer()
# print(f'end2 - start2: {end2 - start2}')