# P1720 月落乌啼算钱（斐波那契数列） https://www.luogu.com.cn/problem/P1720

# from typing import List

n = int(input())

# f = (((1 + 5**0.5) / 2)**n - ((1 - 5**0.5) / 2)**n) / 5**0.5

# table = [0] * (n + 1)  # type: List[int]
# if n > 0:
#     table[1] = 1

# for i in range(2, n + 1):
#     table[i] = table[i - 1] + table[i - 2]

if n in (0, 1):
    print('%.2f' % n)
    exit()

a = 0
b = 1
while n > 2:
    b, a = a + b, b
    n -= 1

print('%.2f' % (a + b))
