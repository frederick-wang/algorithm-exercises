# P3392 涂国旗 https://www.luogu.com.cn/problem/P3392

N, M = map(int, input().split())
# 预处理每一行改变为三种颜色的代价
costs = [{'W': 0, 'B': 0, 'R': 0} for _ in range(N)]
for i in range(N):
    row = input().strip()
    for color in ('W', 'B', 'R'):
        costs[i][color] = M - row.count(color)
# N * M 最大为 2500，是可能的最大代价
min_cost = 2500


def dfs(i: int, color: str, cost: int):
    global min_cost
    cost += costs[i][color]
    if i == N - 1:
        min_cost = min(min_cost, cost)
        return
    if color == 'W':
        if i < N - 3:
            dfs(i + 1, color, cost)
        dfs(i + 1, 'B', cost)
    elif color == 'B':
        if i < N - 2:
            dfs(i + 1, color, cost)
        dfs(i + 1, 'R', cost)
    else:
        dfs(i + 1, color, cost)


dfs(0, 'W', 0)
print(min_cost)
