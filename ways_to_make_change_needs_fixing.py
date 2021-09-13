def numberOfWaysToMakeChange(space, coins):
  #subproblems from 0 to space+1
  subprobs = [0] * (space+1)
  #1 way if 0 space needs to be filled
  subprobs[0] = 1
  already_used_combos = set()
  
  #go through all subproblems
  for subspace in range(1, len(subprobs)):
    already_used_combos.clear()
    curr_num_of_ways = 0
    #go through all possible coin options in order to find its leftover space sub-
    #problem, as long as this space combo has not been done for the subspace
    #we will take the leftover subspace as the num of ways for subspace
    for k in range(len(coins)):
      coin_space = coins[k]
      #if item fits
      if coin_space <= subspace:
        leftover_space = subspace - coin_space
        #find the space combo, can proceed if combo is unique
        space_combo = frozenset({coin_space, leftover_space})
        if space_combo not in already_used_combos:
          curr_num_of_ways += subprobs[leftover_space]
          #add this combo as already used
          already_used_combos.add(space_combo)
    #once we have num of ways, just set that to subspace
    subprobs[subspace] = curr_num_of_ways
  #here done with whole process, answer last in subproblems
  return subprobs[-1]
