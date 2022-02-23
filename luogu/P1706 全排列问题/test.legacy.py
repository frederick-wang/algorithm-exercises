# P1706 全排列问题 https://www.luogu.com.cn/problem/P1706

N = int(input())
result = [0] * N
nums = [True] * (N + 1)

templ = '% 5d' * N


def dfs(i: int):
    if i == N:
        print(templ % tuple(result))
        return
    for j in range(1, N + 1):
        if nums[j]:
            result[i] = j
            nums[j] = False
            dfs(i + 1)
            nums[j] = True


dfs(0)
