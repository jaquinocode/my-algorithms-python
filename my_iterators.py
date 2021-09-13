from itertools import tee, chain

# run this file for a showcase of how these iterators I made work

def prev_curr_iter(iterable):
    # ABC -> (None, A) (A, B) (B, C)
    a, b = tee(iterable)
    return zip(chain([None], a), b)

for prev, curr in prev_curr_iter("ABC"):
    print(f"{prev=}\t{curr=}")
print()

def prev_curr_after_iter(iterable):
    # ABC -> (None, A, B) (A, B, C) (B, C, None)
    a, b, c = tee(iterable, 3)
    next(c, None)
    return zip(chain([None], a), b, chain(c, [None]))

for prev, curr, after in prev_curr_after_iter(""):
    print(f"{prev=}\t{curr=}\t{after=}")
print()