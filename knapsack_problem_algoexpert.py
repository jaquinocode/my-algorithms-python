#o(c*w), c is choices, w is weight limit
def knapsackProblem(items, capacity):
  if len(items) == 0 or capacity == 0: return [0, []]

  #create 2d array, each cell's supposed to have array, items * capac
  #item locations array that satisfy the cell
  rows_amount, columns_amount = len(items), capacity
  grid = [[list() for _ in range(columns_amount)] for _ in range(rows_amount)]


  #i is row, k is column
  for i in range(rows_amount):
    curr_item_value, curr_item_weight = items[i]
    for k in range(columns_amount):
      curr_cell_limit = k + 1
      #start by inheriting cell from above, fill w/ [] if no cell above
      grid[i][k] = grid[i-1][k] if i-1 >= 0 else []

      #check if I can fit the item into cell
      if curr_item_weight <= curr_cell_limit:
        #try to make best possible combo of items to beat inherited combo
        #add curr item loc to our best combo & see how much space is leftover
        best_items_locs = [i]
        leftover_weight = curr_cell_limit - curr_item_weight
        #if there's space, add the appropriate fitting item from cell from row above
        if leftover_weight > 0:
          extra_best_items_locs = grid[i-1][leftover_weight-1] if i-1 >= 0 else []
          best_items_locs.extend(extra_best_items_locs)  #bug: you append elements and extend lists
                                                         #here you appended instead of extending

        #if this new value beats the inherited value, then replace it
        #find value of both
        curr_cell_value = get_total_value(grid[i][k], items)
        best_items_value = get_total_value(best_items_locs, items)
        if best_items_value > curr_cell_value:
          grid[i][k] = best_items_locs
      #if I can't put curr_item in, just go to next loop

  #once I'm done with all cells, lowest rightmost cell has best item combo
  items_locs_solution = grid[-1][-1]
  items_locs_solution.reverse()  #so I can pass algoexpert's bad tests
  items_locs_solution_value = get_total_value(items_locs_solution, items)
  return [items_locs_solution_value, items_locs_solution]


def get_total_value(items_locs, items):
  total_value = 0
  #go through specific items, accumulating total value of all specific items
  for i in items_locs:
    total_value += items[i][0]
  return total_value


def knapsackProblemNoComments(items, capacity):
  if len(items) == 0 or capacity == 0: return [0, []]

  rows_amount, columns_amount = len(items), capacity
  grid = [[list() for _ in range(columns_amount)] for _ in range(rows_amount)]

  for i in range(rows_amount):
    curr_item_value, curr_item_weight = items[i]
    for k in range(columns_amount):
      curr_cell_limit = k + 1
      grid[i][k] = grid[i-1][k] if i-1 >= 0 else []

      if curr_item_weight <= curr_cell_limit:
        best_items_locs = [i]
        leftover_weight = curr_cell_limit - curr_item_weight
        if leftover_weight > 0:
          extra_best_items_locs = grid[i-1][leftover_weight-1] if i-1 >= 0 else []
          best_items_locs.extend(extra_best_items_locs)
        if get_value(best_items_locs, items) > get_value(grid[i][k], items):
          grid[i][k] = best_items_locs

  items_locs_solution = grid[-1][-1]
  items_locs_solution_value = get_total_value(items_locs_solution, items)
  return [items_locs_solution_value, items_locs_solution]

print(knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 0))