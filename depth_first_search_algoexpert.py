class Node:
  def __init__(self, name):
    self.children = []
    self.name = name

  def addChild(self, name):
    self.children.append(Node(name))
    return self

  def depthFirstSearch(self, array):
    traversed = []
    curr_node = None
    #add first elem to stack
    stack = [self]
    while stack:
      #get a from stack
      curr_node = stack.pop() #good job on calling it curr_node instead of curr

      #proccess it, add to traversed
      traversed.append(curr_node.name)

      #add children of a , from right to left, have to do this to get a more 
      #unnatural left to right traversal,
      #adding normally gives as expected right to left traversal instead
      stack.extend(curr_node.children[::-1])
    #here traversed should be done
    return traversed
