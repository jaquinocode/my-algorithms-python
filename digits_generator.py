from math import log10

# digs in left-to-right order
def digits(n):
    digs_to_keep = digs_count(n) - 1
    head = None
    body = n
    for digs_to_keep in range(digs_to_keep, -1, -1):
        head, body = divmod(body, 10**digs_to_keep)
        yield head
# digs from right-to-left order
def digits_rev(n):
    if n == 0:
        yield 0
        return

    while n > 0:
        n, last = divmod(n, 10)
        yield last

def digs_count(n):
    return int(log10(n) + 1) if n else 1


for dig in digits(120):
    print(dig)
print()
for dig in digits_rev(120):
    print(dig)