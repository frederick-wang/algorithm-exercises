# P3405 [USACO16DEC]Cities and States S https://www.luogu.com.cn/problem/P3405

from typing import Dict

N = int(input())
d: Dict[str, Dict[str, int]] = {}
ans = 0
for _ in range(N):
    city, state = input().split()
    city = city[:2]
    if city == state:
        continue
    if city in d and state in d[city]:
        ans += d[city][state]
    if state in d:
        if city in d[state]:
            d[state][city] += 1
        else:
            d[state][city] = 1
    else:
        d[state] = {city: 1}
print(ans)
