def findK(number, power):
  sum = 0  # is this necessary? YES
  digits = listOfDigits(number)

  for i, digit in enumerate(digits):
    sum += digit**power  # is this the way to do it?
    power += 1

  k = sum / number
  # if its 2.00 it will be considered integer
  kIsPosInteger = (k > 0) and (k % 1 == 0)
  if kIsPosInteger:
    return int(k)
  else:
    return -1


def listOfDigits(number):
  stack = []
  digits = []

  if number == 0:
    return [0]

  while number > 0:
    stack.append(number % 10)
    number = number // 10

  for i in range(len(stack)):
    digits.append(stack.pop())

  return digits


print(findK(345, 2))