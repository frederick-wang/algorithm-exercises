# P1873 [COCI 2011/2012 #5] EKO / 砍树 https://www.luogu.com.cn/problem/P1873

import numpy as np

N, M = map(int, input().split())
heights = np.fromstring(input(), dtype=np.int32, sep=' ')
ub = np.max(heights)
lb = 0


def f(x: int) -> int:
    diff = heights - x
    return np.sum(diff[diff > 0])


while lb <= ub:
    m = (lb + ub) // 2
    fm = f(m)
    if fm < M:
        ub = m - 1
    elif fm > M:
        lb = m + 1
    else:
        print(m)
        exit()
print(ub)
