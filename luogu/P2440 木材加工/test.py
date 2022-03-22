# P2440 木材加工 https://www.luogu.com.cn/problem/P2440

import numpy as np

N, K = map(int, input().split())
L = np.zeros(N, dtype=np.int32)
for i in range(N):
    L[i] = int(input())

if np.sum(L) < K:
    print(0)
    exit()


def f(l: int) -> int:
    return np.sum(L // l)


lb = 1
ub = np.max(L)
while lb <= ub:
    m = (lb + ub) >> 1
    fm = f(m)  # 能切出 fm 段的木材
    if fm < K:
        ub = m - 1
    else:
        lb = m + 1
print(ub)
