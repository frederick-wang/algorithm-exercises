# P1957 口算练习题 https://www.luogu.com.cn/problem/P1957

from operator import add, sub, mul
from typing import Callable, Dict

i = int(input())

op_func = {
    'a': add,
    'b': sub,
    'c': mul
}  # type: Dict[str, Callable[[int, int], int]]
op_str = {'a': '+', 'b': '-', 'c': '*'}

op = ''
while i:
    raw_input = input().strip().split()
    if len(raw_input) == 3:
        op = raw_input[0]
        n1 = int(raw_input[1])
        n2 = int(raw_input[2])
    else:
        n1 = int(raw_input[0])
        n2 = int(raw_input[1])
    s = '%d%s%d=%d' % (n1, op_str[op], n2, op_func[op](n1, n2))
    print(s)
    print(len(s))
    i -= 1
