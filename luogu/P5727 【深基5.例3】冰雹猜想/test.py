# P5727 【深基5.例3】冰雹猜想

from typing import List

seq = []  # type: List[int]
n = int(input())

while n > 1:
    seq.append(n)
    n = 3 * n + 1 if n % 2 else n // 2

print(1, *reversed(seq))
