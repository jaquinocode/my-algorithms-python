def index_of(target, array):
  start = 0
  end = len(array) - 1
  target_index = binary_search(target, array, start, end)
  return target_index

def binary_search(target, array, start, end):
  midIndex = start + abs(start - end)//2
  if (start > end):
    return -1
  elif target == array[midIndex]:
    return midIndex
  elif target > array[midIndex]:
    start = midIndex + 1
    return binary_search(target, array, start, end)
  elif target < array[midIndex]:
    end = midIndex - 1
    return binary_search(target, array, start, end)

print(index_of('zamboni', ['aardvark', 'apple', 'boy', 'train', 'zebra']))