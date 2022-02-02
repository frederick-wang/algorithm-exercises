# P1217 [USACO1.5]回文质数 Prime Palindromes https://www.luogu.com.cn/problem/P1217
from typing import List
from array import array

a, b = map(int, input().split())

table_len = 100000
table = array('B', [1]) * (table_len + 1)
table[0] = 0
table[1] = 0
for i in range(4, table_len + 1, 2):
    table[i] = 0
n = 3
while n * n <= table_len:
    if table[n]:
        for i in range(n * n, table_len + 1, n):
            table[i] = 0
    n += 2


def is_prime(n):  # type: (int) -> bool
    if n == 0:
        return False
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n <= table_len:
        return bool(table[n])
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


b_len = len(str(b))

if a <= 2 <= b:
    print(2)

if a <= 3 <= b:
    print(3)

if a <= 5 <= b:
    print(5)

if a <= 7 <= b:
    print(7)

i = 1
while i <= b_len:
    half_len = i // 2
    j = 1
    res = []  # type: List[str]
    new_res = []  # type: List[str]
    final_res = []  # type: List[int]
    while j <= half_len:
        if j == 1:
            for k in range(1, 10, 2):
                res.append(str(k))
        else:
            new_res = []
            for k in range(0, 10):
                new_res += [m + str(k) for m in res]
            res = new_res
        j += 1
    if i % 2 == 0:
        final_res = sorted([int(r + r[::-1]) for r in res])
    else:
        new_res = []
        for k in range(0, 10):
            new_res += [r + str(k) + r[::-1] for r in res]
        final_res = sorted([int(x) for x in new_res])
    for p in filter(lambda x: a <= x <= b and is_prime(x), final_res):
        print(p)
    i += 1
