from collections import deque

#o(v + e) or o(n) t, o(largest_river) s, num of nodes in the largest river
def riverSizes(grid):
  river_sums = []
  #go through grid, row by row
  for row_i in range(len(grid)):
    for col_i in range(len(grid[0])):
      cell_value = grid[row_i][col_i]
      #if 1, traverse graph
      if cell_value == 1:
        #traverse the river while replacing 1s w/ 0s, return sum
        curr_river_sum = find_river_sum((row_i, col_i), grid)
        river_sums.append(curr_river_sum)
      #else go to next cell
  return river_sums


def find_river_sum(start_loc, grid):
  river_sum = 0
  que_history = set()
  que = deque()
  que.append(start_loc)
  que_history.add(start_loc)
  #breadth first search, for each cell, process, then add potentially 4 children
  while que:
    row_i, col_i = que.popleft()
    #process, increment sum, rewrite cell value as 0
    river_sum += 1
    grid[row_i][col_i] = 0
    #add potentially 4 children, left, right, top, then bottom
    for r_i, c_i in [(row_i, col_i-1), (row_i, col_i+1), (row_i-1, col_i), 
                         (row_i+1, col_i)]:
      child_loc = (r_i, c_i)
      indices_valid = 0 <= r_i < len(grid) and 0 <= c_i < len(grid[0])
      child_value = grid[r_i][c_i] if indices_valid else 0
      #must keep note if node ever at all added to que before to prevent double adds
      if child_value == 1 and child_loc not in que_history:
        que.append(child_loc)
        que_history.add(child_loc)
  return river_sum
