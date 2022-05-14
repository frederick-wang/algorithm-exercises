# P5076 【深基16.例7】普通二叉树（简化版） https://www.luogu.com.cn/problem/P5076

import bisect
from typing import List

Q = int(input())
nums: List[int] = []

for _ in range(Q):
    opt, x = map(int, input().split())
    if opt == 1:
        print(bisect.bisect_left(nums, x) + 1)
    elif opt == 2:
        print(nums[x - 1])
    elif opt == 3:
        i = bisect.bisect_left(nums, x)
        print(nums[i - 1] if i else -2147483647)
    elif opt == 4:
        i = bisect.bisect_right(nums, x)
        print(2147483647 if i == len(nums) else nums[i])
    else:
        nums.insert(bisect.bisect_left(nums, x), x)
