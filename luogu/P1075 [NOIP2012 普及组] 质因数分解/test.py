# P1075 [NOIP2012 普及组] 质因数分解 https://www.luogu.com.cn/problem/P1075

# from array import array
# from math import ceil

# TABLE_LEN = 45000
# table = array('b', [1]) * (TABLE_LEN + 1)
# table[0] = 0
# table[1] = 0
# for i in range(4, (TABLE_LEN + 1), 2):
#     table[i] = 0
# i = 3
# while i * i <= TABLE_LEN:
#     if table[i]:
#         for j in range(i * i, (TABLE_LEN + 1), i):
#             table[j] = 0
#     i += 2

# n = int(input())

# nums = [x for x in range(ceil(n**0.5)) if table[x] and n % x == 0]

# print(n // nums[0])

n = int(input())

if n % 2 == 0:
    print(n // 2)
i = 3
while i * i <= n:
    if n % i == 0:
        print(n // i)
        break
    i += 2
