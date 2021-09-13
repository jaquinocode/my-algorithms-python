def reverse_number_bits(num):
  reversed_num = 0
  last_bit = 0
  #loop, stop when you've removed the last bit from num 32 times
  for _ in range(32):
    #last bit of num
    last_bit = num & 1
    #and append that bit to our sol bits
    #make room for it first by shifting
    reversed_num = reversed_num << 1
    #actually append bit
    reversed_num = reversed_num ^ last_bit
    #remove our last bit from num so we can easily get next bit on next loop
    #we do this by shifting
    num = num >> 1
  #here reversed_num should have all bits removed and appended
  return reversed_num

reverse_number_bits(4294967293)