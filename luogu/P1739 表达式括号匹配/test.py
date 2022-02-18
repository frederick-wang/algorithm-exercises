# P1739 表达式括号匹配 https://www.luogu.com.cn/problem/P1739

from collections import deque
from typing import Deque

que: Deque[bool] = deque()

try:
    s = input()
except:
    print('NO')
    exit()

for c in s:
    if c == '@':
        break
    if c == '(':
        que.append(True)
    elif c == ')':
        if len(que):
            que.pop()
        else:
            print('NO')
            exit()

print('NO' if que else 'YES')
