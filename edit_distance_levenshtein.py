def levenshteinDistance(s1, s2):
  def row_char(row_i):
    return s1[row_i-1]

  def col_char(col_i):
    return s2[col_i-1]
  #subprobs[1][1] will denote subprob for s1[0] & s2[0]
  #strings are in weak system, subprobs in strong system
  subprobs = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]
  initialize_base_cases(subprobs)

  #iterate left to right, row by row, ignoring 1st row & 1st col
  for row_i in range(1, len(subprobs)):
    for col_i in range(1, len(subprobs[0])):
      #if both letters at this subp cell match, just inherit topleft cell
      if row_char(row_i) == col_char(col_i):
        subprobs[row_i][col_i] = subprobs[row_i-1][col_i-1]
      #else if they don't match, add 1 to minimum of top, left, & topleft cells
      else:
        subprobs[row_i][col_i] = 1 + min(subprobs[row_i][col_i-1], 
                                 subprobs[row_i-1][col_i-1], subprobs[row_i-1][col_i])
  #once i'm here, solved everything
  return subprobs[-1][-1]


def initialize_base_cases(subprobs):
  #1st row & 1st col should be 0 1 2 3 etc
  for i in range(len(subprobs[0])):
    subprobs[0][i] = i
  for i in range(len(subprobs)):
    subprobs[i][0] = i


print(levenshteinDistance('jerkaderkdek', 'hellopam'))