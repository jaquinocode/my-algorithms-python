def minNumberOfCoinsForChange(space, coins):
  #edge case handling
  if space == 0: return 0
  #make array from 0 to space
  subprobs = [0] * (space+1)
  
  #go through each cell in subprobs, start from 1 to end
  for curr_space in range(1, len(subprobs)):
    #go through all poss options, and find contribution for each one
    #then get min contribution from all poss options seen
    min_contribution = float('inf')
    for k in range(len(coins)):
      #if it fits
      coin_space = coins[k]
      if coin_space <= curr_space:
        leftover_space = curr_space - coin_space
        curr_contribution = 1 + subprobs[leftover_space]
        #todo:some type of checking for combos that can't fill space fully
        #if they can't, then don't include them in calculation
      
        min_contribution = min(curr_contribution, min_contribution)

    #found min contribution, just put contribution as our subprobs val
    subprobs[curr_space] = min_contribution
  #once we're here, last elem in subprobs should be min cost for space
  return subprobs[-1] if subprobs[-1] not in [0, float('inf')] else -1
