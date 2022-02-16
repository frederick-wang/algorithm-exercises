# P1786 帮贡排序 https://www.luogu.com.cn/problem/P1786

from typing import List


class Member:
    name: str
    title: str
    contrib: int
    level: int
    idx: int

    def __init__(self, name: str, title: str, contrib: int, level: int,
                 idx: int):
        self.name = name
        self.title = title
        self.contrib = contrib
        self.level = level
        self.idx = idx


TITLE = {
    'BangZhu': 1,
    'FuBangZhu': 2,
    'HuFa': 3,
    'ZhangLao': 4,
    'TangZhu': 5,
    'JingYing': 6,
    'BangZhong': 7
}

n = int(input())

members: List[Member] = []

for i in range(n):
    raw = input().strip().split()
    members.append(Member(raw[0], raw[1], int(raw[2]), int(raw[3]), i))

others = sorted(members[3:], key=lambda x: (-x.contrib, x.idx))
for i, m in enumerate(others):
    if i < 2:
        m.title = 'HuFa'
    elif i < 6:
        m.title = 'ZhangLao'
    elif i < 13:
        m.title = 'TangZhu'
    elif i < 38:
        m.title = 'JingYing'
    else:
        m.title = 'BangZhong'

for m in members[:3]:
    print(m.name, m.title, m.level)

for m in sorted(others, key=lambda x: (TITLE[x.title], -x.level, x.idx)):
    print(m.name, m.title, m.level)
