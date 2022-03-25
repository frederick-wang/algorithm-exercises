# P4387 【深基15.习9】验证栈序列 https://www.luogu.com.cn/problem/P4387

from collections import deque
from typing import Deque

Q = int(input())
for _ in range(Q):
    N = int(input())
    seq_in = map(int, input().split())
    seq_out = deque(map(int, input().split()))
    stack: Deque[int] = deque()
    for i in seq_in:
        stack.appendleft(i)
        while len(stack) and stack[0] == seq_out[0]:
            stack.popleft()
            seq_out.popleft()
    if len(stack):
        print('No')
    else:
        print('Yes')
