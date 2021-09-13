from collections import defaultdict

def four_number_sum(numbers, target):
  pairs_history = defaultdict(set)
  four_sums_indices = set()
  for i in range(len(numbers)-1):
    for k in range(i+1, len(numbers)):
      curr_sum = numbers[i] + numbers[k]
      leftover = target - curr_sum
      curr_indices_pair = frozenset({i, k})
      
      #if there's a eligible pair then get quad and add to solution
      for eligible_pair in pairs_history[leftover]:
        quadruplet = eligible_pair | curr_indices_pair
        if len(quadruplet) == 4:
          #add quad to result
          four_sums_indices.add(quadruplet)
      #add 2-combo to history
      pairs_history[curr_sum].add(curr_indices_pair)
  #convert four_sums_indices to desired format
  #which is a list of lists
  return four_sums_indices


print(four_number_sum([7, 6, 4, -1, 1, 2], 16))