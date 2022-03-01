# P1928 外星密码 https://www.luogu.com.cn/problem/P1928

from typing import Dict, List

S = input().strip()

stack: List[str] = []
mem: Dict[str, str] = {}


def f(s: str) -> str:
    if s not in mem:
        i = 1
        num = 0
        result: List[str] = []
        end = len(s) - 1
        while i < end:
            c = s[i]
            if not c.isdigit():
                break
            num = 10 * num + int(c)
            i += 1
        sb_num = 0
        sb: List[str] = []
        for c in s[i:]:
            if c == '[':
                sb_num += 1
                sb.append(c)
            elif c == ']':
                sb_num -= 1
                sb.append(c)
                if not sb_num:
                    result.append(f(''.join(sb)))
                    sb.clear()
            else:
                if not sb_num:
                    result.append(c)
                else:
                    sb.append(c)
        mem[s] = num * ''.join(result)
    return mem[s]


result: List[str] = []
sb_num = 0
sb: List[str] = []
for c in S:
    if c == '[':
        sb_num += 1
        sb.append(c)
    elif c == ']':
        sb_num -= 1
        sb.append(c)
        if not sb_num:
            result.append(f(''.join(sb)))
            sb.clear()
    else:
        if not sb_num:
            result.append(c)
        else:
            sb.append(c)

print(''.join(result))
