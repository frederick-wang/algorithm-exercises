# P1603 斯诺登的密码 https://www.luogu.com.cn/problem/P1603

from typing import List
from itertools import permutations

sentence = input().replace('.', '').strip().lower().split()

d = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'a': 1,
    'both': 2,
    'another': 1,
    'first': 1,
    'second': 2,
    'third': 3
}

nums = []  # type: List[str]

is_num_existed = False
for word in sentence:
    if word in d:
        if not is_num_existed:
            is_num_existed = True
        nums.append(str(d[word]**2 % 100).rjust(2, '0'))

if not is_num_existed:
    print(0)
    exit()

min_num = 969696969696

for new_nums in permutations(nums):
    new_num = int(''.join(nums))
    if new_num < min_num:
        min_num = new_num

print(min_num)
