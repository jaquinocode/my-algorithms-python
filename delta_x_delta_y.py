def is_inside(x, y):
  # check if inside 31 w x 11 l
  return 0 <= x <= 30 and 0 <= y <= 10


# words = input().split()
# 11x31
# expected ans was 30 & 10? or 10 & 31?
dirs = ['ts', 'ts', 'ding', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'bing', 'bing', 'bing', 'bing', 'bing', 'bing', 'bing', 'bing', 'bing', 'boom', 'bing', 'bing', 'bing', 'bing', 'bing', 'bing', 'bing', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom', 'boom']


x_delta = {
    "ts": -1,
    "boom": 1,
    "ding": 0,
    "bing": 0,
}
y_delta = {
    "ts": 0,
    "boom": 0,
    "ding": -1,
    "bing": 1,
}
print(dirs)
curr_x = 0
curr_y = 0

for dir in dirs:
    # change curr_pos based on that direction
    new_x = curr_x + x_delta[dir]
    new_y = curr_y + y_delta[dir]

    if is_inside(new_x, new_y):
        curr_x, curr_y = new_x, new_y

print(curr_x, curr_y)
