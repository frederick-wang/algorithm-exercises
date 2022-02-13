# P1116 车厢重组 https://www.luogu.com.cn/problem/P1116

from typing import List

N = int(input())
seq: List[int] = []
while len(seq) < N:
    seq += list(map(int, input().split()))
num = 0
cycle_num = 0

i = 0
is_sorted = True
while True:
    if seq[i] > seq[i + 1]:
        is_sorted = False
        seq[i], seq[i + 1] = seq[i + 1], seq[i]
        num += 1
    if i < N - cycle_num - 2:
        i += 1
    else:
        if is_sorted:
            break
        else:
            i = 0
            is_sorted = True
            cycle_num += 1

print(num)
