import traceback

def index_of(target, array):
  if (array is None) or (target is None):
    return -1

  start = 0
  end = len(array) - 1
  
  while not(start > end):
    midIndex = findMidIndex(start, end)
    if target == array[midIndex]:
      return midIndex
    elif target > array[midIndex]:
      start = midIndex + 1
    elif target < array[midIndex]:
      end = midIndex - 1
    else:
      return -1

  return -1

def findMidIndex(start, end):
  midIndex = start + abs(start - end)//2
  return midIndex

print(index_of('apple', [1, 2, 4]))