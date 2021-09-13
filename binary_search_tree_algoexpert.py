from collections import deque

class BST:
  def __init__(self, value, parent=None):
    self.value = value
    self.left = None
    self.right = None
    self.parent = parent

  def get_child(self, direction):
    if direction == 'left':
      return self.left
    elif direction == 'right':
      return self.right

  def set_child(self, direction, value):
    if direction == 'left':
      self.left = BST(value, self) if type(value) == int else value
    elif direction == 'right':
      self.right = BST(value, self) if type(value) == int else value

  def get_direction(self):
    direction = ''
    children = [self.parent.left, self.parent.right]
    for i in range(len(children)):
      if children[i] is self:
        direction = 'left' if i == 0 else 'right'
    return direction

  def insert(self, value):
    curr = self
    direction = ''
    while not(curr is None):
      last_node_accessed = curr
      direction = 'left' if curr.value > value else 'right'
      curr = curr.get_child(direction)
    last_direction = direction
    last_node_accessed.set_child(last_direction, value)

    return self

  def contains(self, target):
    curr = self
    target_found = False
    while not(curr is None or target_found):
      if curr.value == target:
        target_found = True
        break
      direction = 'left' if curr.value > target else 'right'
      curr = curr.get_child(direction)
    return target_found

  def remove(self, value):
    curr = self
    remove_complete = False
    while not(curr is None or remove_complete):
      if curr.value == value:
        self = self.remove_node(curr)
        remove_complete = True
        break
      direction = 'left' if curr.value > value else 'right'
      curr = curr.get_child(direction)
    return self

  def remove_node(self, node):
    num_of_children = self.get_num_of_children(node)

    #case of no children
    if num_of_children == 0:
      if node is self: #node is head
        self = None
      else:
        #break the parent link
        node.parent.set_child(node.get_direction(), None)

    #case of 1 child
    elif num_of_children == 1:
      if node is self: #node is head
        for nodes_child in (node.left, node.right):
          if nodes_child:
            self = nodes_child
      else:
        for nodes_child in (node.left, node.right):
          if nodes_child:
            node.parent.set_child(node.get_direction(), nodes_child)
  
    #case of 2 children
    elif num_of_children == 2:
      #overwrite child value and delete successor
      min_successor_node = self.get_min_successor(node)
      node.value = min_successor_node.value
      self = self.remove_node(min_successor_node)

    return self

  def get_num_of_children(self, node):
    return sum(1 for child in (node.left, node.right) if child)

  def get_min_successor(self, node):
    #root of the subbranch where i want to find my min node
    curr = node.right
    
    while not(curr is None):
      last_node_accessed = curr
      curr = curr.left
    return last_node_accessed