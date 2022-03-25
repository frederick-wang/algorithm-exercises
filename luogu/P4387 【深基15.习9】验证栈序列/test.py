# P4387 【深基15.习9】验证栈序列 https://www.luogu.com.cn/problem/P4387

from collections import deque
from typing import Deque

Q = int(input())
for _ in range(Q):
    N = int(input())
    seq_in = deque(map(int, input().split()))
    seq_out = deque(map(int, input().split()))
    stack: Deque[int] = deque()
    while len(seq_out):
        if len(stack) and stack[0] == seq_out[0]:
            stack.popleft()
            seq_out.popleft()
        elif len(seq_in):
            stack.appendleft(seq_in.popleft())
        else:
            print('No')
            break
    else:
        print('Yes')
