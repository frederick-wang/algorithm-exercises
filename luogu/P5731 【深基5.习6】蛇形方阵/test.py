# P5731 【深基5.习6】蛇形方阵 https://www.luogu.com.cn/problem/P5731

n = int(input())

s = [[0] * n for _ in range(n)]

# up, down, left, right: 0, 1, 2, 3
direction = 3
# Delta
d = [(0, -1), (0, 1), (-1, 0), (1, 0)]

x = 0
y = 0
for i in range(1, n**2 + 1):
    s[y][x] = i
    if direction == 3 and (x == n - 1 or s[y][x + 1]):
        direction = 1
    elif direction == 1 and (y == n - 1 or s[y + 1][x]):
        direction = 2
    elif direction == 2 and (x == 0 or s[y][x - 1]):
        direction = 0
    elif direction == 0 and (y == 0 or s[y - 1][x]):
        direction = 3
    x += d[direction][0]
    y += d[direction][1]

for row in s:
    for num in row:
        print('% 3d' % num, end='')
    print()
