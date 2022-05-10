# P2814 家谱 https://www.luogu.com.cn/problem/P2814

from typing import Dict

f: Dict[str, str] = {}


def find(x: str) -> str:
    if x != f[x]:
        f[x] = find(f[x])
    return f[x]


ancestor = ''
while True:
    raw_input = input().strip()
    if raw_input == '$':
        exit()
    action = raw_input[0]
    name = raw_input[1:]
    if name not in f:
        f[name] = name
    if action == '#':
        ancestor = name
    elif action == '+':
        f[find(name)] = find(ancestor)
    else:
        print(name, find(name))
