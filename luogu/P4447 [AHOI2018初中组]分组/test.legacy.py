# P4447 [AHOI2018初中组]分组 https://www.luogu.com.cn/problem/P4447

from typing import Dict

n = int(input())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
counts: Dict[int, int] = {}
for num in nums:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
last_num = 0
last_cnt = 0
res = 0
min_res = 100000
is_first = True
while n:
    for num, cnt in counts.items():
        if not cnt:
            continue
        if is_first:
            is_first = False
            last_num = num
            last_cnt = cnt
            res = 1
            counts[num] -= 1
            n -= 1
        else:
            if num == last_num - 1 and cnt >= last_cnt:
                res += 1
                last_num = num
                last_cnt = cnt
                counts[num] -= 1
                n -= 1
            else:
                break
    min_res = min(min_res, res)
    is_first = True
print(min_res)
