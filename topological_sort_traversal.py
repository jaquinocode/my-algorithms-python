#we have adjacency dict, w/ children as sets
""" my ex
0   1
 \ /
  2
  |
  3    0, 1, 2, 3 or 1, 0, 2, 3
"""
#o(bm) space, b is branch factor, m is depth
#o(v+e) time
def get_proper_traversal(edges):
  curr_num = None
  traversed_nums = []

  graph = to_adjacency_dict_with_requirements(edges) #o(n) t
  eligible_start_nums = get_start_nums(graph) #o(n) t
  stack = [num for num in eligible_start_nums]
  while stack:
    #get guy from pop stack
    curr_num = stack.pop()

    #process that guy #add to traversed nodes
    traversed_nums.append(curr_num)

    #add the dude's allowed children to stack
    #for each child he has, remove all linkage from parent & child, then check
    # if child is
    #independant
    for child in graph[curr_num]['children']:
      #below commented out line makes sense but not needed since we'll make sure
      # we don't add nodes to stack more than once
      #graph[curr_num]['children'].remove(child)
      graph[child]['requirements'] -= 1

      #if child independant, aka has no parents, then its allowed to go into
      # stack
      if graph[child]['requirements'] <= 0:
        stack.append(child)

  return traversed_nums
  



def get_start_nums(graph):
