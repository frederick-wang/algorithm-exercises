# P2058 [NOIP2016 普及组] 海港 https://www.luogu.com.cn/problem/P2058

from collections import deque
from typing import Deque
from typing import Counter, Dict

N = int(input())
records: Deque[Counter[str]] = deque()
record: Dict[str, int] = {}
ans = 0
t: Deque[int] = deque()
start_i = 0
result = ''

for _ in range(N):
    raw_input = input().split()
    t_i = int(raw_input[0])
    t.append(t_i)
    c = Counter(raw_input[2:])
    records.append(c)
    for k, v in c.items():
        if k in record:
            record[k] += v
        else:
            record[k] = v
            ans += 1
    while t[0] + 86400 <= t_i:
        for k, v in records.popleft().items():
            record[k] -= v
            if not record[k]:
                ans -= 1
                del record[k]
        t.popleft()
    result += f'{ans}\n'
print(result, end='')
