# P1068 [NOIP2009 普及组] 分数线划定 https://www.luogu.com.cn/problem/P1068

from typing import List, Tuple

N, M = map(int, input().split())
l: List[Tuple[int, int]] = []
for _ in range(N):
    k, s = map(int, input().split())
    l.append((-s, k))
l.sort()
line = l[M * 15 // 10 - 1][0]
out_str = ''
num = 0
for s, k in l:
    if s > line:
        break
    out_str += f'{k} {-s}\n'
    num += 1
print(-line, num)
print(out_str, end='')
