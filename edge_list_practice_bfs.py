from collections import deque

#edges is sorted list of tuples >> [('A', 'B'), ('A', 'C'), ...]
def breadth_first_traversal(edges): 
  if not edges: return []

  traversed = []
  que = deque([edges[0][0]])
  bookmark = 0
  while que:
    #pop off start of que
    curr_letter = que.popleft()

    #process
    traversed.append(curr_letter)

    #add node's children to que    
    for i in range(bookmark, len(edges)):
      edge = edges[i]
      parent, child = edge[0], edge[1]
      if parent == curr_letter:
        que.append(child)
        bookmark += 1
      else:
        #curr letter's children over
        break
  return traversed


edges = [
  ('A', 'B'),
  ('A', 'C'),
  ('A', 'D'),
  ('B', 'E'),
  ('B', 'F'),
  ('D', 'G'),
]
print(breadth_first_traversal(edges))