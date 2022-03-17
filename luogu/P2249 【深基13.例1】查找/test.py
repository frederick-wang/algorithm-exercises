# P2249 【深基13.例1】查找 https://www.luogu.com.cn/problem/P2249
# https://www.luogu.com.cn/record/71633433

import bisect

N, M = map(int, input().split())
nums = list(map(int, input().split()))
query = list(map(int, input().split()))
for q in query:
    i = bisect.bisect_left(nums, q)
    if i < N and nums[i] == q:
        print(i + 1, end=' ')
    else:
        print(-1, end=' ')
print()
