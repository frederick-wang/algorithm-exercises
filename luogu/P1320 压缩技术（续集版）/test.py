# P1320 压缩技术（续集版） https://www.luogu.com.cn/problem/P1320

from typing import List

lines = []  # type: List[int]
n = 0

while True:
    try:
        raw_input = input().strip()
        if not raw_input:
            break
    except:
        break
    n += 1
    lines = lines + list(map(int, raw_input))

print(n, end='')

consecutive_num = 0
num = 0
for i in lines:
    if i == num:
        consecutive_num += 1
    else:
        print(' %d' % consecutive_num, end='')
        num = 1 - num
        consecutive_num = 1
print(' %d' % consecutive_num)
