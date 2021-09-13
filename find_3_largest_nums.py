#o(n) time
#o(1) space
def findThreeLargestNumbers(numbers):
  #pass through and find 1st max, then find 2nd max ignoring 1st max elem, etc
  max_nums = []
  max_nums_locations = []
  for _ in range(3): #o(n) done 3 times
    next_max_loc = find_max_loc_filtered(numbers, max_nums_locations)
    max_nums.append(numbers[next_max_loc])
    max_nums_locations.append(next_max_loc)
  max_nums.reverse()

  return max_nums


def find_max_loc_filtered(numbers, filtered_indices):
  max = -float('inf')
  max_loc = None
  for i in range(len(numbers)):
    if i not in filtered_indices:
      if numbers[i] > max:
        max = numbers[i]
        max_loc = i
  return max_loc
