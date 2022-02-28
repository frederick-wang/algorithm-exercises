# P1464 Function https://www.luogu.com.cn/problem/P1464
# https://www.luogu.com.cn/record/70293156

from typing import Dict, Tuple

mem: Dict[Tuple[int, int, int], int] = {}
result = ''


def w(a: int, b: int, c: int) -> int:
    param = (a, b, c)
    if param not in mem:
        if a <= 0 or b <= 0 or c <= 0:
            mem[param] = 1
        elif a > 20 or b > 20 or c > 20:
            mem[param] = w(20, 20, 20)
        elif a < b and b < c:
            mem[param] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        else:
            mem[param] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(
                a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return mem[param]


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    result += f'w({a}, {b}, {c}) = {w(a,b,c)}\n'
print(result, end='')
