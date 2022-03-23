# P3613 【深基15.例2】寄包柜 https://www.luogu.com.cn/problem/P3613

from typing import Dict, List

N, Q = map(int, input().split())
cabinets: List[Dict[int, int]] = [{} for _ in range(N)]

for _ in range(Q):
    raw_input = list(map(int, input().split()))
    t = raw_input[0]
    if t == 2:
        i, j = raw_input[1:]
        print(cabinets[i - 1][j])
    else:
        i, j, k = raw_input[1:]
        cabinets[i - 1][j] = k
