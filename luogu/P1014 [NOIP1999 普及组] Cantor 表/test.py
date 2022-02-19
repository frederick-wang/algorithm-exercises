# P1014 [NOIP1999 普及组] Cantor 表 https://www.luogu.com.cn/problem/P1014

from math import ceil

N = int(input())
n = ceil((-1 + (1 + 8 * N)**0.5) / 2)
diff = (n + 1) * n // 2 - N
pos = n - diff
rev = 1 + diff
print(f'{rev}/{pos}' if n % 2 else f'{pos}/{rev}')
