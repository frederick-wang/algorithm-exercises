# P5250 【深基17.例5】木材仓库 https://www.luogu.com.cn/problem/P5250

from sys import stdin
from typing import List
from bisect import bisect_left

N = int(stdin.readline())
wood: List[int] = []
for _ in range(N):
    op, length = map(int, stdin.readline().split())
    if op == 1:
        i = bisect_left(wood, length)
        if i < len(wood) and wood[i] == length:
            print('Already Exist')
        else:
            wood.insert(i, length)
    elif l := len(wood):
        i = bisect_left(wood, length)
        if i < l and wood[i] == length:
            print(length)
            wood.pop(i)
        else:
            i1 = max(0, i - 1)
            i2 = min(l - 1, i)
            if abs(wood[i1] - length) <= abs(wood[i2] - length):
                print(wood[i1])
                wood.pop(i1)
            else:
                print(wood[i2])
                wood.pop(i2)
    else:
        print('Empty')
