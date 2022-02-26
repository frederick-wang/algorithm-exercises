# P2036 [COCI2008-2009#2] PERKET https://www.luogu.com.cn/problem/P2036
# https://www.luogu.com.cn/record/70179511

N = int(input())
# [酸度, 苦度]
ingredients = [tuple(map(int, input().split())) for _ in range(N)]


def dfs(i: int, a: int, b: int) -> int:
    if i == N:
        if a == 1 and not b:
            return 1000000000
        return abs(a - b)
    i_a, i_b = ingredients[i]
    return min(dfs(i + 1, a, b), dfs(i + 1, a * i_a, b + i_b))


print(dfs(0, 1, 0))
