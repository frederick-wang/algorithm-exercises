# P1024 [NOIP2001 提高组] 一元三次方程求解 https://www.luogu.com.cn/problem/P1024

from typing import List, Optional

PRECISION = 1e-3
A, B, C, D = map(float, input().split())


def f(x: float) -> float:
    return A * x**3 + B * x**2 + C * x + D


def solve(a: float, b: float) -> Optional[float]:
    m = (a + b) / 2
    if b - a < PRECISION:
        return m
    fm = f(m)
    if f(a) * fm <= 0:
        return solve(a, m)
    # 不找右端点，不然会重复
    if fm * f(b) < 0:
        return solve(m, b)
    return None


roots: List[float] = []
for i in range(-100, 101):
    if (r := solve(i, i + 1)):
        roots.append(r)
        if len(roots) == 3:
            break
print('%.2f %.2f %.2f' % tuple(roots))
