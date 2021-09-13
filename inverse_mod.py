factor = int(input())
lower_bound, upper_bound  = sorted([int(input()), int(input())])

# get the lowest possible multiple (of factor) within our bounds
# mod usually gives lower multiple so do inverse mod instead to get higher bound
first_multiple = lower_bound + (-lower_bound % factor)
print(" ".join(str(i) for i in range(first_multiple, upper_bound+1, factor)))
