class BSTNode:
  def __init__(self, value, parent=None):
    self.value = value
    self.children = {'left': None, 'right': None}
    self.parent = parent

  def get_child(self, direction):
    return self.children[direction]

  def set_child(self, direction, value):
    current_child = self.children[direction]
    if current_child:
      current_child.parent = None
    self.children[direction] = BSTNode(value, self)

  def set_child_to_node(self, direction, node):
    current_child = self.children[direction]
    if current_child:
      current_child.parent = None
    self.children[direction] = node
    self.children[direction].parent = self

  def set_child_to_none(self, direction):
    current_child = self.children[direction]
    if current_child:
      current_child.parent = None
    self.children[direction] = None


class BST:
  def __init__(self, iterable=None):
    self.head = None
    if iterable is not None:
      for e in iterable:
        self.insert(e)

  def get_direction(self, node):
    if node.parent is None: return None

    left_or_right = None
    for direction in ('left', 'right'):
      #former bug, below line had 'is node' say 'is self' instead
      #because it used to be that self literally was the node in question
      #after switching to 2 classes, this was no longer true
      #and maybe i forgot to change it or didn't see it when converting it
      #so that self is not used and node is used instead
      if node.parent.children[direction] is node:
        left_or_right = direction
        break
    return left_or_right

  def insert(self, value):
    if self.head is None:
      self.head = BSTNode(value)
      return

    curr = self.head
    direction = ''
    last_node_accessed = None
    while not(curr is None):
      last_node_accessed = curr
      direction = 'left' if curr.value > value else 'right'
      curr = curr.get_child(direction)
    last_direction = direction
    last_node_accessed.set_child(last_direction, value)

  def contains(self, target):
    if self.head == None: return False

    curr = self.head
    target_found = False
    while not(curr is None or target_found):
      if curr.value == target:
        target_found = True
        break
      direction = 'left' if curr.value > target else 'right'
      curr = curr.get_child(direction)
    return target_found

  def remove(self, value):
    if self.head == None: return

    curr = self.head
    remove_complete = False
    while not(curr is None or remove_complete):
      if curr.value == value:
        self.remove_node(curr)
        remove_complete = True
        break
      direction = 'left' if curr.value > value else 'right'
      curr = curr.get_child(direction)

  def remove_node(self, node):
    num_of_children = self.get_num_of_children(node)

    #case of no children
    if num_of_children == 0:
      if node is self.head:
        self.head = None
      else:
        #break the link from parent to child
        node.parent.set_child_to_none(self.get_direction(node))

    #case of 1 child
    elif num_of_children == 1:
      for nodes_child in node.children.values():
        if nodes_child:
          if node is self.head:
            nodes_child.parent = None
            self.head = nodes_child
          else:
            node.parent.set_child_to_node(self.get_direction(node),
                                          nodes_child)
  
    #case of 2 children
    elif num_of_children == 2:
      #overwrite node value w/ successor and delete successor
      min_successor_node = self.get_min_successor(node)
      node.value = min_successor_node.value
      self.remove_node(min_successor_node)

  def get_num_of_children(self, node):
    return sum(1 for child in node.children.values() if child)

  def get_min_successor(self, node):
    #right of node is root of the subbranch where i want to find my min node
    curr = node.get_child('right')
    while not(curr is None):
      last_node_accessed = curr
      curr = curr.get_child('left')
    return last_node_accessed



import unittest

test1 = BST([10, 5, 15, 5, 2, 14, 22])

test2 = BST([10, 15, 11, 22])
test2.remove(10)

test3 = BST([10, 5, 7, 2])
test3.remove(10)

test4 = BST([10, 5, 15, 22, 17, 34, 7, 2, 5, 1, 35, 27, 16, 30])
test4.remove(22)
test4.remove(17)

# test4 = (
#     BST(10)
#     .insert(5)
#     .insert(15)
#     .insert(22)
#     .insert(17)
#     .insert(34)
#     .insert(7)
#     .insert(2)
#     .insert(5)
#     .insert(1)
#     .insert(35)
#     .insert(27)
#     .insert(16)
#     .insert(30)
#     .remove(22)
#     .remove(17)
# )


def inOrderTraverse(node, array):
    if node is not None:
        inOrderTraverse(node.get_child('left'), array)
        array.append(node.value)
        inOrderTraverse(node.get_child('right'), array)
    return array


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(test1.head.get_child('left').value, 5)

    def test_case_2(self):
        self.assertEqual(test1.head.get_child('right').get_child('right').value, 22)

    def test_case_3(self):
        self.assertEqual(test1.head.get_child('right').get_child('left').value, 14)

    def test_case_4(self):
        self.assertEqual(test1.head.get_child('left').get_child('right').value, 5)

    def test_case_5(self):
        self.assertEqual(test1.head.get_child('left').get_child('left').value, 2)

    def test_case_6(self):
        self.assertEqual(test1.head.get_child('left').get_child('left').get_child('left'), None)

    def test_case_7(self):
        self.assertEqual(test1.head.get_child('right').get_child('left').get_child('right'), None)

    def test_case_8(self):
        self.assertEqual(test1.contains(15), True)

    def test_case_9(self):
        self.assertEqual(test1.contains(2), True)

    def test_case_10(self):
        self.assertEqual(test1.contains(5), True)

    def test_case_11(self):
        self.assertEqual(test1.contains(10), True)

    def test_case_12(self):
        self.assertEqual(test1.contains(22), True)

    def test_case_13(self):
        self.assertEqual(test1.contains(23), False)

    def test_case_14(self):
        self.assertEqual(inOrderTraverse(test2.head, []), [11, 15, 22])

    def test_case_15(self):
        self.assertEqual(inOrderTraverse(test3.head, []), [2, 5, 7])

    def test_case_16(self):
        self.assertEqual(inOrderTraverse(test4.head, []), [1, 2, 5, 5, 7, 10, 15, 16, 27, 30, 34, 35])

    def test_case_17(self):
        self.assertEqual(test4.head.get_child('right').get_child('right').value, 27)

    def test_case_18(self):
        self.assertEqual(test4.head.get_child('right').get_child('right').get_child('left').value, 16)


if __name__ == "__main__":
    unittest.main()