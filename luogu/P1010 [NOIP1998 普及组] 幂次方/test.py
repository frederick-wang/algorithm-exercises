# P1010 [NOIP1998 普及组] 幂次方 https://www.luogu.com.cn/problem/P1010

from typing import List

N = int(input())
mem = [''] * 20001


def k2(num: int) -> str:
    if not num:
        return '0'
    if not mem[num]:
        result: List[str] = []
        b_k = bin(num)
        b_k_len = len(b_k)
        for i, c in enumerate(b_k):
            if i > 1:
                if c == '1':
                    k = b_k_len - i - 1
                    k_str = '' if k == 1 else f'({k2(k)})'
                    result.append(f'2{k_str}')
        mem[num] = '+'.join(result)
    return mem[num]


print(k2(N))
