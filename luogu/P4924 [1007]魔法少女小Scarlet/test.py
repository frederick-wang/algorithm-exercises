# P4924 [1007]魔法少女小Scarlet https://www.luogu.com.cn/problem/P4924
# type: ignore

import numpy as np

n, m = map(int, input().split())
s = np.arange(1, n**2 + 1, dtype=np.uint32).reshape(n, n)


def rotate(x: int, y: int, r: int, z: int):
    x1 = x - r
    x2 = x + r + 1
    y1 = y - r
    y2 = y + r + 1
    sub_s = s[x1:x2, y1:y2]
    s[x1:x2, y1:y2] = sub_s.T[::-1] if z else sub_s.T[:, ::-1]


for _ in range(m):
    x, y, r, z = map(int, input().split())
    rotate(x - 1, y - 1, r, z)

for row in s:
    print(' '.join(map(str, row)))
