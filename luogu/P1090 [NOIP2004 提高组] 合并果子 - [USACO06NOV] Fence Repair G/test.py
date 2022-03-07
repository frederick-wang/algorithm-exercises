# P1090 [NOIP2004 提高组] 合并果子 / [USACO06NOV] Fence Repair G https://www.luogu.com.cn/problem/P1090
# https://www.luogu.com.cn/record/70844866

from heapq import heapify, heappop, heappush

N = int(input())
nums = list(map(int, input().split()))
result = 0
heapify(nums)
while len(nums) > 1:
    a = heappop(nums)
    b = heappop(nums)
    s = a + b
    result += s
    heappush(nums, s)
print(result)
