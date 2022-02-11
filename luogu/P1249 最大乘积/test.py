# P1249 最大乘积 https://www.luogu.com.cn/problem/P1249

from functools import reduce
from typing import List

n = int(input())

if n == 3:
    print(1, 2)
    print(2)
    exit()

if n == 4:
    print(1, 3)
    print(3)
    exit()

nums: List[int] = []
s = 0
i = 2
while True:
    if s + i > n:
        break
    s += i
    nums.append(i)
    i += 1

diff = n - s
i = len(nums) - 1
while diff:
    nums[i] += 1
    i -= 1
    diff -= 1

print(*nums)
print(reduce(lambda acc, cur: acc * cur, nums, 1))
