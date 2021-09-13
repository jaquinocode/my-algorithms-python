from itertools import tee, chain

def prev_curr_iter(iterable):
    # ABC >> (None, A) (A, B) (B, C)
    a, b = tee(iterable)
    return zip(chain([None], a), b)

def max_contiguous_char_freq(s):
    curr_count = 0
    max_count = 0
    for prev, curr in prev_curr_iter(s):
        if prev != curr:
            curr_count = 0
        curr_count += 1
        max_count = max(max_count, curr_count)
    return max_count

print(max_contiguous_char_freq("11223333"))