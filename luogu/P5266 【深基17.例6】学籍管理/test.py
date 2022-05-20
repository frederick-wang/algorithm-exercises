# P5266 【深基17.例6】学籍管理 https://www.luogu.com.cn/problem/P5266

import sys
from typing import Dict

d: Dict[str, str] = {}
cnt = 0

N = int(sys.stdin.readline())
for _ in range(N):
    raw_input = sys.stdin.readline().strip().split()
    op = raw_input[0]
    if op == '1':
        name = raw_input[1]
        if name not in d:
            cnt += 1
        d[name] = raw_input[2]
        print('OK')
    elif op == '2':
        print(d.get(raw_input[1], 'Not found'))
    elif op == '3':
        if (name := raw_input[1]) in d:
            del d[name]
            cnt -= 1
            print('Deleted successfully')
        else:
            print('Not found')
    else:
        print(cnt)
