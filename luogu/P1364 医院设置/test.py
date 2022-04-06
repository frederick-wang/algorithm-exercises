# P1364 医院设置 https://www.luogu.com.cn/problem/P1364

from typing import Iterator, List, Optional, Tuple


class Edge:
    to: int
    cost: int

    def __init__(self, to: int, cost: int):
        self.to = to
        self.cost = cost

    def __repr__(self) -> str:
        return f'Edge(to={self.to}, cost={self.cost})'

    def __iter__(self) -> Iterator[int]:
        return iter([self.to, self.cost])


N = int(input())
p: List[List[Edge]] = [[] for _ in range(N + 1)]


def index(x: int) -> Optional[Edge]:
    for i in range(1, N + 1):
        for e in p[i]:
            if e.to == x:
                return e
    return None


edges: List[Tuple[int, int]] = []
weights = [0] * (N + 1)
for i in range(1, N + 1):
    w, u, v = map(int, input().split())
    weights[i] = w
    if u:
        edges.extend(((i, u), (u, i)))
    if v:
        edges.extend(((i, v), (v, i)))
for f, t in edges:
    p[f].append(Edge(t, weights[t]))


def dfs(x: int, d: int) -> int:
    vis[x] = True
    return sum(cost * d + dfs(to, d + 1) for to, cost in p[x] if not vis[to])


min_distance = int(1e9)
for i in range(1, N + 1):
    vis = [False] * (N + 1)
    min_distance = min(min_distance, dfs(i, 1))
print(min_distance)
