# P1518 [USACO2.4]两只塔姆沃斯牛 The Tamworth Two https://www.luogu.com.cn/problem/P1518

from typing import Set, Tuple

directions = {'N': (0, -1), 'S': (0, 1), 'W': (-1, 0), 'E': (1, 0)}
next_directions = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
state_records: Set[Tuple[int, int, str, int, int, str]] = set()

john_pos = (0, 0)
john_direction = 'N'
cow_pos = (0, 0)
cow_direction = 'N'

grids = [['.'] * 10 for _ in range(10)]


def is_no_obstacle(x: int, y: int) -> bool:
    return 0 <= x <= 9 and 0 <= y <= 9 and grids[y][x] != '*'


for i in range(10):
    grids[i] = list(input().strip())
    if 'F' in grids[i]:
        john_pos = (grids[i].index('F'), i)
    if 'C' in grids[i]:
        cow_pos = (grids[i].index('C'), i)

t = 0

while True:
    john_dx, john_dy = directions[john_direction]
    john_new_x = john_pos[0] + john_dx
    john_new_y = john_pos[1] + john_dy
    if is_no_obstacle(john_new_x, john_new_y):
        john_pos = (john_new_x, john_new_y)
    else:
        john_direction = next_directions[john_direction]
    cow_dx, cow_dy = directions[cow_direction]
    cow_new_x = cow_pos[0] + cow_dx
    cow_new_y = cow_pos[1] + cow_dy
    if is_no_obstacle(cow_new_x, cow_new_y):
        cow_pos = (cow_new_x, cow_new_y)
    else:
        cow_direction = next_directions[cow_direction]
    t += 1
    state = (john_pos[0], john_pos[1], john_direction, cow_pos[0], cow_pos[1],
             cow_direction)
    if state in state_records:
        print(0)
        exit()
    else:
        state_records.add(state)
    if john_pos == cow_pos:
        break

print(t)
