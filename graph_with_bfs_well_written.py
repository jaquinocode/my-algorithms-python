from collections import deque
from collections import defaultdict

class Graph:
  def __init__(self, name=None):
    self.children = defaultdict(list)
    self.head_name = name

  def add_child(self, parent_name, child_name):
    if self.graph_empty(): self.head_name = parent_name
    self.children[parent_name].append(child_name)
    return self

  def add_children(self, parent_name, children):
    if self.graph_empty(): self.head_name = parent_name
    #add children names to parents children
    self.children[parent_name].extend(children)
    return self

  def get_bfs_list(self):
    #navigate through tree w/ bfs, logging every node I process into a list and return it
    if self.graph_empty(): return []

    traversed_nodes = []
    curr_name = ''
    queue = deque([self.head_name])
    while queue: #stop when queue is empty
      #add queue left elem to curr
      curr_name = queue[0]

      #add curr node to traversed list
      traversed_nodes.append(curr_name)

      #add all of curr's children to queue
      queue.extend(self.children[curr_name])

      #popleft the curr from the queue
      queue.popleft()
    #should have complete list
    return traversed_nodes

  def graph_empty(self):
    return self.head_name is None
