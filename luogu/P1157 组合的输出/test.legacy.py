# P1157 组合的输出 https://www.luogu.com.cn/problem/P1157

N, R = map(int, input().split())
result = [0] * (R + 1)

templ = '% 3d' * R


def dfs(i: int):
    if i > R:
        print(templ % tuple(result[1:]))
        return
    for j in range(result[i - 1] + 1, N + 1):
        result[i] = j
        dfs(i + 1)


dfs(1)
