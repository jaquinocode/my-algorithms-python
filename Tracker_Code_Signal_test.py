from collections import defaultdict

class Tracker():
  def __init__(self):
    self.allocated_nums = defaultdict(set)

  def allocate(self, host_alpha):
    hostname = ""
    for i in range(1, 1000):
      if i not in self.allocated_nums[host_alpha]:
        hostname = host_alpha + str(i)
        self.allocated_nums[host_alpha].add(i)
        return hostname
    return "couldnt find eligible hostname allocation"
    
  def deallocate(self, hostname):
    for i, c in enumerate(hostname):
      if c.isdigit():
        found_index = i

    host_alpha = hostname[:found_index]
    num = int(hostname[found_index:])
    self.allocated_nums[host_alpha].discard(num)

# query >> "A myhostalpha" >> ["myhostalpha1"]
def hostAllocation(queries):
    tracker = Tracker()
    ans = []
    for query in queries:
        task = query.split(' ')
        if task[0] == 'A':
            ans.append(tracker.allocate(task[1]))
        if task[0] == 'D':
            tracker.deallocate(task[1])
    return ans
