# P1135 奇怪的电梯 https://www.luogu.com.cn/problem/P1135

from collections import deque
from typing import Deque

N, A, B = map(int, input().split())
k_list = [0] + list(map(int, input().split()))
cnt = [-1] * (N + 1)
que: Deque[int] = deque()
que.append(A)
cnt[A] = 0

while len(que):
    f = que.popleft()
    if f == B:
        break
    k = k_list[f]
    nf = f + k
    if 1 <= nf <= N and cnt[nf] == -1:
        cnt[nf] = cnt[f] + 1
        que.append(nf)
    nf = f - k
    if 1 <= nf <= N and cnt[nf] == -1:
        cnt[nf] = cnt[f] + 1
        que.append(nf)

print(cnt[B])
