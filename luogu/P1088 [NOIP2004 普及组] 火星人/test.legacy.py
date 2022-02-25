# P1088 [NOIP2004 普及组] 火星人 https://www.luogu.com.cn/problem/P1088
# https://www.luogu.com.cn/record/69995865

# 琢磨了一晚上想出的方法，一查发现原来这个方法叫康托展开……

from typing import List

N = int(input())
m = int(input())
nums = list(map(int, input().split()))

factorials: List[int] = [1] * N
for i in range(1, N):
    factorials[i] = factorials[i - 1] * i

remains = list(range(1, N + 1))
for i, n in enumerate(nums):
    nums[i] = (serial_num := remains.index(n))
    del remains[serial_num]

for i in range(N):
    f = factorials[N - 1 - i]
    nums[i] += m // f
    m %= f

for i in range(N - 1, 0, -1):
    upper_bound = N - i
    while nums[i] >= upper_bound:
        nums[i] -= upper_bound
        nums[i - 1] += 1

remains = list(range(1, N + 1))
for i, s_n in enumerate(nums):
    nums[i] = remains[s_n]
    del remains[s_n]

print(' '.join(map(str, nums)))
