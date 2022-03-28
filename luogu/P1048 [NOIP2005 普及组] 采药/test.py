# P1048 [NOIP2005 普及组] 采药 luogu.com.cn/problem/P1048

T, M = map(int, input().split())
t = [0] * M
v = [0] * M
for i in range(M):
    t[i], v[i] = map(int, input().split())
mem = [[0] * (T + 1) for _ in range(M)]


def dfs(i: int, st: int) -> int:
    if i == M:
        return 0
    if not mem[i][st]:
        if st + t[i] > T:
            mem[i][st] = dfs(i + 1, st)
            return mem[i][st]
        mem[i][st] = max(dfs(i + 1, st), dfs(i + 1, st + t[i]) + v[i])
    return mem[i][st]


print(dfs(0, 0))
