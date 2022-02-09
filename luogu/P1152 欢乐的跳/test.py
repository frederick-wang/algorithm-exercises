# P1152 欢乐的跳 https://www.luogu.com.cn/problem/P1152

from typing import Dict

raw = map(int, input().split())
n, nums = next(raw), list(raw)

diffs: Dict[int, bool] = {}
for i in range(1, n):
    diff = abs(nums[i] - nums[i - 1])
    diffs[diff] = True

is_jolly = True
for i in range(1, n):
    if i not in diffs:
        is_jolly = False
        break

print('Jolly' if is_jolly else 'Not jolly')
