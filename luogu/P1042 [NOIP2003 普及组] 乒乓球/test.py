# P1042 [NOIP2003 普及组] 乒乓球 https://www.luogu.com.cn/problem/P1042

from typing import List

record_11: List[List[int]] = [[0, 0]]
record_21: List[List[int]] = [[0, 0]]

is_loop = True
while is_loop:
    raw_input = input().strip()
    idx = raw_input.find('E')
    if idx == -1:
        result = raw_input
    else:
        result = raw_input[:idx]
        is_loop = False
    for i in result:
        if i == 'W':
            record_11[-1][0] += 1
            record_21[-1][0] += 1
        elif i == 'L':
            record_11[-1][1] += 1
            record_21[-1][1] += 1

        if (record_11[-1][0] >= 11 or record_11[-1][1] >= 11
           ) and abs(record_11[-1][0] - record_11[-1][1]) >= 2:
            record_11.append([0, 0])

        if (record_21[-1][0] >= 21 or record_21[-1][1] >= 21
           ) and abs(record_21[-1][0] - record_21[-1][1]) >= 2:
            record_21.append([0, 0])

for rec in record_11:
    print(f'{rec[0]}:{rec[1]}')
print()
for rec in record_21:
    print(f'{rec[0]}:{rec[1]}')
