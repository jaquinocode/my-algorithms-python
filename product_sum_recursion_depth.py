def productSum(array, depth=1):
  #if no depth given in arg, say depth is 1

  #say that the sum is 0, you'll increment it as you go through array
  #go through each elem, and if normal elem, increment w/ depth * whatever it is
  sum = 0
  for e in array:
    if isinstance(e, int): # elem normal
      #just increment it
      sum += e
    elif isinstance(e, list): #elem is special, use recursion
      sum += productSum(e, depth + 1)

  return depth * sum


# space o(max_depth)
# time o(n), n is amount of integers
