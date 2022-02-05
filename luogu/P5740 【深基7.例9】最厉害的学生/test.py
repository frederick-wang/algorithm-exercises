# P5740 【深基7.例9】最厉害的学生 https://www.luogu.com.cn/problem/P5740

from typing import Tuple

n = int(input())

max_sum = 0
max_stu = ('', 0, 0, 0)  # type: Tuple[str, int, int, int]
for i in range(n):
    raw = input().strip().split()
    name, scores = raw[0], tuple(map(int, raw[1:]))
    sum_score = sum(scores)
    if sum_score > max_sum or i == 0:
        max_sum = sum_score
        max_stu = (name, scores[0], scores[1], scores[2])
print(*max_stu)
