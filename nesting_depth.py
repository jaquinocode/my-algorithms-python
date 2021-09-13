#input is going to be like [2,2,3,2,2,1], all ints
def nesting_depth(numbers):
  parens_debt = 0
  #insert (s to beginning, as many as 1st elems num is
  for _ in range(numbers[0]):
    numbers.insert(0, '(')
    parens_debt += 1
  i = 0
  i = go_to_next_number(i, numbers)

  #loop, stop when i is -1 (aka we're out of bounds)
  while not(i == -1):
    curr_num = numbers[i]
    next_num = numbers[i+1] if i+1 < len(numbers) else -1
    if next_num == -1: #if we reached out of bounds
      i = -1
      continue

    difference = abs(next_num - curr_num)
    if next_num == curr_num:
      i += 1
      continue
    elif next_num > curr_num:
      for _ in range(difference):
        numbers.insert(i+1, '(')
      parens_debt += difference
    elif next_num < curr_num:
      for _ in range(difference):
        numbers.insert(i+1, ')')
      parens_debt -= difference

    #keep iterating until find number or we go out of bounds
    #gives -1 if we reached out of bounds, which can't happen theoretically
    i = go_to_next_number(i+1, numbers)
  #end loop, we've reached out of bounds, time to append our load
  for _ in range(parens_debt):
    numbers.append(')')
  #turn all elems to strings and join to make the result
  res = ''.join(str(e) for e in numbers)
  return res


def go_to_next_number(start_i, numbers):
  for i in range(start_i, len(numbers)):
    if isinstance(numbers[i], int):
      return i
  return -1


#input
res = []
tests = int(input())
for i in range(1, tests+1):
  input_string = input()
  numbers_input = [int(char) for char in list(input_string)]
  res_string = nesting_depth(numbers_input)
  res.append("Case #{}: {}".format(i, res_string))
#output
for case_line in res:
  print(case_line)
