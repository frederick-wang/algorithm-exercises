# P4924 [1007]魔法少女小Scarlet https://www.luogu.com.cn/problem/P4924
# 用 PyPy3 提交，不然会超时

from array import array

n, m = map(int, input().split())
N2 = n**2
s = array('I', [0]) * N2
sub_s = array('I', [0]) * N2
for i in range(N2):
    s[i] = i + 1


def rotate(x: int, y: int, r: int, z: int):
    l = 2 * r + 1
    x1 = x - r
    x2 = x + r
    y1 = y - r
    y2 = y + r
    for i in range(l):
        for j in range(l):
            old_x = x1 + i
            old_y = y1 + j
            sub_s[i * l + j] = s[old_x * n + old_y]
    if z:
        for i in range(l):
            for j in range(l):
                new_x = x2 - j
                new_y = y1 + i
                s[new_x * n + new_y] = sub_s[i * l + j]
    else:
        for i in range(l):
            for j in range(l):
                new_x = x1 + j
                new_y = y2 - i
                s[new_x * n + new_y] = sub_s[i * l + j]


for _ in range(m):
    x, y, r, z = map(int, input().split())
    rotate(x - 1, y - 1, r, z)

for i in range(N2):
    print(s[i], end='\n' if i % n == n - 1 else ' ')
