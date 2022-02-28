# P1044 [NOIP2003 普及组] 栈 https://www.luogu.com.cn/problem/P1044

N = int(input())
mem = [[0] * (N + 1) for _ in range(N + 1)]


def dfs(i: int, stack_num: int) -> int:
    if i == N:
        return 1
    if not mem[i][stack_num]:
        for j in range(1, stack_num + 2):
            mem[i][stack_num] += dfs(i + 1, j)
    return mem[i][stack_num]


print(dfs(1, 1))
