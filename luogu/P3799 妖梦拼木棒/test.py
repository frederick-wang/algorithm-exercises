# P3799 妖梦拼木棒 https://www.luogu.com.cn/problem/P3799
# 用 PyPy3 提交: https://www.luogu.com.cn/record/70263691

from collections import Counter
from typing import List

N = int(input())
nums: List[int] = []
while nums.__len__() < N:
    nums += list(map(int, input().split()))
nums.sort()
counter = Counter(nums)
result = 0
i = 0
while i < N:
    a = nums[i]
    a_cnt = counter[a]
    if a_cnt > 1:
        c1_cnt = counter[2 * a]
        if c1_cnt > 1:
            result += c1_cnt * (c1_cnt - 1) * a_cnt * (a_cnt - 1) >> 2
    j = i + a_cnt
    while j < N:
        b = nums[j]
        b_cnt = counter[b]
        c_cnt = counter[a + b]
        if c_cnt > 1:
            result += c_cnt * (c_cnt - 1) * a_cnt * b_cnt >> 1
        j += b_cnt
    i += a_cnt
print(result % 1000000007)
