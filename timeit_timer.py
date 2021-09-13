import timeit


setup = '''
from llist import dllist, dllistnode
import random

l1 = [1, 2, 3]
l2 = [4, 5, 6]
for i in range(5000):
  r = random.randint(1, 100000)
  l1.append(r)
  r = random.randint(1, 100000)
  l2.append(r)

ll1 = dllist([1, 2, 3])
ll2 = dllist([4, 5, 6])
for i in range(5000):
  r = random.randint(1, 100000)
  ll1.append(r)
  r = random.randint(1, 100000)
  ll2.append(r)
ll3 = dllist()
ll4 = dllist()
'''

time1 = min(
    timeit.Timer('l3 = l1.copy(); l4 = l2.copy()',
                 setup=setup).repeat(7, 1000))
print(f'time 1: {time1}')

time2 = min(
    timeit.Timer('ll1.last.value = 956; ll1.last.value = 42',
                 setup=setup).repeat(7, 1000))
print(f'time 2: {time2}')

print(f'time2 - time1: {time2 - time1}')