from math import ceil

# cost and production
c = int(input("c: "))
p = int(input("p: "))
# max possible profit after 100 turns for c=10 and p=1: 32904

turns_til_worth_it = ceil(c / p)
turn_boundary = 100 - turns_til_worth_it
machines = 1
gold = 0
for turn in range(1, 101):
    gold += machines*p

    # buy all the machines i can as long as Im before a boundary, aka when its worth it
    worth_it = turn <= turn_boundary
    if gold >= c and worth_it:
      machines_i_can_buy = gold // c

      gold -= c*machines_i_can_buy
      machines += machines_i_can_buy

print(gold)