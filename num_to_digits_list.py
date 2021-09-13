def to_digits(number):
  digits = list()
  digit_position = num_of_digits(number) - 1
  
  while digit_position >= 0:
    digit = (number // 10**digit_position) % 10
    digits.append(digit)
    digit_position -= 1
  return digits

def num_of_digits(number):
  if number == 0: return 1
  count = 0
  while number > 0:
    number = number // 10
    count += 1
  return count

print(to_digits(0))