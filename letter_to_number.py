def letter_to_number(letter):
  letter_number = ord(letter) - ord('a')
  return letter_number

print(letter_to_number('z'))