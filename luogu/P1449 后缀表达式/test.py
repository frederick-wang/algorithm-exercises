# P1449 后缀表达式 https://www.luogu.com.cn/problem/P1449

from collections import deque
from typing import Deque

s: Deque[int] = deque()
tmp = ''
for c in input():
    if c == '@':
        break
    if c.isdigit():
        tmp += c
    elif c == '.':
        s.append(int(tmp))
        tmp = ''
    elif c == '+':
        o2 = s.pop()
        o1 = s.pop()
        s.append(o1 + o2)
    elif c == '-':
        o2 = s.pop()
        o1 = s.pop()
        s.append(o1 - o2)
    elif c == '*':
        o2 = s.pop()
        o1 = s.pop()
        s.append(o1 * o2)
    elif c == '/':
        o2 = s.pop()
        o1 = s.pop()
        s.append(o1 // o2)
print(s.pop())
