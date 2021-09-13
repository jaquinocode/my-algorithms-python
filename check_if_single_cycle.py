#o(n) t, o(n) s
def has_single_cycle_storing_traversed(numbers):
  if len(numbers) == 0: return False

  traversed_indices = set()
  #ending condition: you've traversed already traversed index, if this index is start 
  #index then instead check if all indices traversed and if not then its false
  #plan: from start i: go through each index and mark traversed, check if back at start
  #w/ aforementioned check & also if traversed already
  #loop, stop when index repeated
  start_i = 0
  i = start_i
  while not(i in traversed_indices):
    #add i to traversed
    traversed_indices.add(i)
    #read number
    curr_jump = numbers[i]
    #add that number to i
    i += curr_jump
    #wrap i appropriately
    i = i % len(numbers)
  #here, we handle ending conditions after we find a repeatedly visited index
  #if all indices traversed, then return true
  return len(traversed_indices) == len(numbers) if i == start_i else False


#o(n) t, o(1) s
#good lesson to learn with the use of back_at_start as something meaningful
#that makes our code clearer than clement's at algoexpert.io
def hasSingleCycle(numbers):
  elements_visited = 0
  start_i = 0
  i = start_i
  back_at_start = False
  #stop when either you've visited len(numbers) elems or you're back at the start
  while not(elements_visited == len(numbers) or back_at_start):
    elements_visited += 1
    i = next_i(i, numbers)
    
    back_at_start = i == start_i
  #if prematurely reached start_i then check if its accessed everything
  #if accessed everything, check if at start_i
  return elements_visited == len(numbers) and back_at_start


def next_i(i, numbers):
  return (i + numbers[i]) % len(numbers)
