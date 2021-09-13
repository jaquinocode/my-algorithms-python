def smallest_difference(array1, array2):
  array1.sort()
  array2.sort()
  i1 = 0
  i2 = 0
  smallest = float('inf')
  current = float('inf')
  smallest_pair = []
  while not(i1 >= len(array1) or i2 >= len(array2)):
    num1, num2 = array1[i1], array2[i2]
    current = abs(num1 - num2)

    if num1 == num2:
      return [num1, num2]
    elif num1 < num2:
      i1 += 1
    elif num2 < num1:
      i2 += 1

    if current < smallest:
      smallest = current
      smallest_pair = [num1, num2]

  return smallest_pair
