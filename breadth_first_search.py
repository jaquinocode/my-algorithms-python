from collections import defaultdict, deque


def bfs(children, starting_node, target):
  nodes_queue = deque()
  nodes_added = set()
  first_parents = {}

  initialize(starting_node, nodes_queue, nodes_added)
  while nodes_queue:
    node = nodes_queue.popleft()

    if node == target:
      return get_path(target, first_parents)
    for child in children[node]:
      if child not in nodes_added:
        nodes_queue.append(child)
        nodes_added.add(child)
        first_parents[child] = node

  return []


def get_path(target, first_parents):
  path = deque([target])
  current = target
  while current in first_parents:
    current = first_parents[current]
    path.appendleft(current)
  return list(path)


def initialize(starting_node, nodes_queue, nodes_added):
  nodes_queue.append(starting_node)
  nodes_added.add(starting_node)


def empty(object):
  return len(object) <= 0


children = defaultdict(set)
children['cab'] = {'cat', 'car'}
children['cat'] = {'mat', 'bat'}
children['car'] = {'cat', 'bar'}
children['bar'] = {'bat'}
children['mat'] = {'bat'}
starting_node = 'cab'
target = 'bat'

print(bfs(children, starting_node, target))