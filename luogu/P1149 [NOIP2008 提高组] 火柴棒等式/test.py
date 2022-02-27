# P1149 [NOIP2008 提高组] 火柴棒等式 https://www.luogu.com.cn/problem/P1149
# https://www.luogu.com.cn/record/70260851

from typing import Dict

N = int(input())
MAX_NUM = N - 4

matches = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)
matches_num: Dict[int, int] = {}
result = 0


def get_matches_num(n: int):
    if n not in matches_num:
        matches_num[n] = sum(map(matches.__getitem__, map(int, str(n))))
    return matches_num[n]


for a in range(1000):
    a_num = get_matches_num(a)
    if a_num > MAX_NUM:
        continue
    for b in range(1000):
        b_num = get_matches_num(b)
        if a_num + b_num > MAX_NUM:
            continue
        c = a + b
        c_num = get_matches_num(c)
        if a_num + b_num + c_num == MAX_NUM:
            result += 1

print(result)
