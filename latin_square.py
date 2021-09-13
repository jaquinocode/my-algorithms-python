def latin_square(matrix):
  diagonal_sum = find_diagonal_sum(matrix)
  num_of_dirty_rows = 0
  num_of_dirty_cols = 0
  #check amount of rows that have repeats, called dirty row
  for row in matrix:
    num_of_dirty_rows += is_dirty_row(row)

  #check amount of columns that have repeats, called dirty column
  for k in range(len(matrix[0])):
    num_of_dirty_cols += is_dirty_col(k, matrix)

  return diagonal_sum, num_of_dirty_rows, num_of_dirty_cols

def find_diagonal_sum(matrix):
  i, k = 0, 0
  sum = 0
  while not(i == len(matrix)):
    sum += matrix[i][k]

    i += 1
    k += 1
  return sum

def is_dirty_row(row):
  #row is an array [1, 2, 2]
  #put array into a set {1, 2}
  row_set = set(row)
  does_repeat = len(row_set) != len(row)
  return does_repeat

def is_dirty_col(k, matrix):
  #array of column elems
  column = []
  for i in range(len(matrix)):
    column.append(matrix[i][k])
  col_set = set(column)
  does_repeat = len(col_set) != len(column)
  return does_repeat

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
#1
#3
#1 2 3
#3 1 2
#2 3 1
res = []
tests = int(input()) # read a line with a single integer
for i in range(1, tests + 1):
  N = int(input())
  #read N numb of lines
  matrix = [list(map(int, input().split()))  for _ in range(N)]
  sum, dirty_rows, dirty_cols = latin_square(matrix)
  res.append("Case #{}: {} {} {}".format(i, sum, dirty_rows, dirty_cols))
for case_line in res:
  print(case_line)
