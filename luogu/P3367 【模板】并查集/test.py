# P3367 【模板】并查集 https://www.luogu.com.cn/problem/P3367

N, M = map(int, input().split())
f = list(range(N + 1))


def find(x: int):
    if x != f[x]:
        f[x] = find(f[x])
    return f[x]


def union(x: int, y: int):
    f[find(x)] = find(y)


for _ in range(M):
    Z, X, Y = map(int, input().split())
    if Z == 1:
        union(X, Y)
    else:
        print('Y' if find(X) == find(Y) else 'N')
