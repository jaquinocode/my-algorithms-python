#input: [(),(),()]
#output: CJC
def check_if_possible(input_intervals):
  intervals = sorted(input_intervals, key=lambda interval: interval[0])
  smallest = intervals[0][0]
  largest = 24 * 60
  intv_count = 0
  max_count = 0
  for i in range(smallest, largest+1):
    for interval in intervals:
      if interval[0] < i < interval[1]:
        intv_count += 1
    max_count = max(intv_count, max_count)
    intv_count = 0
  if intv_count < 3:
    return True
  else:

    

def scheduler(input_intervals):
  check_if_possible(input_intervals)
  #sort intervals
  intervals = sorted(input_intervals, key=lambda interval: interval[0])
  #assign our intervals
  cs_intervals = []
  js_intervals = []
  assignments = {}
  for interval in intervals:
    c_is_taken = c_taken(interval[0], cs_intervals)
    j_is_taken = j_taken(interval[0], js_intervals)
    if c_is_taken and j_is_taken:
      #impossible
      return 'IMPOSSIBLE'

    if c_is_taken:
      #assign j, goto next intv
      assignments[interval] = 'J'
      js_intervals.append(interval)
    else:
      #assign c
      assignments[interval] = 'C'
      cs_intervals.append(interval)
  #once here, we should have all intv's assigned
  chars = []
  for interval in input_intervals:
    letter = assignments[interval]
    chars.append(letter)
  res = ''.join(chars)
  return res


def c_taken(start_time, cs_intervals):
  for interval in cs_intervals:
    if interval[0] <= start_time < interval[1]:
      return True
  return False

def j_taken(start_time, js_intervals):
  for interval in js_intervals:
    if interval[0] <= start_time < interval[1]:
      return True
  return False

#print(scheduler([(420, 540), (360, 480), (600, 660)]))

#input
res = []
tests = int(input()) # read a line with a single integer
for i in range(1, tests + 1):
  N = int(input())
  #read N numb of lines
  #matrix = [list(map(int, input().split()))  for _ in range(N)]
  intervals = [tuple(map(int, input().split()))  for _ in range(N)]
  res_string = scheduler(intervals)
  res.append("Case #{}: {}".format(i, res_string))
#output
for case_line in res:
  print(case_line)