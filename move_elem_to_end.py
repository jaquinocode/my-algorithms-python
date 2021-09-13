def move_element_to_end(numbers, special_num):
  left_i, right_i = 0, len(numbers) - 1

  while not(left_i >= right_i):
    while not(numbers[left_i] == special_num): #stop when left at special
      left_i += 1
    if numbers[right_i] != special_num: #right at non special number
      #swap
      numbers[left_i], numbers[right_i] = numbers[right_i], numbers[left_i]
      #move in
      left_i += 1
      right_i -= 1
    else:
      #move hopefully to nonspecial num
      right_i -= 1

  return numbers
