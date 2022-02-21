# P1093 [NOIP2007 普及组] 奖学金 https://www.luogu.com.cn/problem/P1093

from typing import List, Tuple

N = int(input())

l: List[Tuple[int, int, int]] = []

for id in range(1, N + 1):
    chinese, math, english = map(int, input().split())
    l.append((chinese + math + english, chinese, -id))
l.sort(reverse=True)
for i in (0, 1, 2, 3, 4):
    s, _, id = l[i]
    print(-id, s)
