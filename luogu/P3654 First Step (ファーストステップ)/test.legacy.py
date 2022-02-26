# P3654 First Step (ファーストステップ) https://www.luogu.com.cn/problem/P3654
# https://www.luogu.com.cn/record/70153804

from typing import Set, Tuple

R, C, K = map(int, input().split())
court = [[''] * C for _ in range(R)]
directions = ((0, -1), (0, 1), (-1, 0), (1, 0))
Pair = Tuple[int, int]
# (开始点, 结束点)
Method = Tuple[Pair, Pair]
methods: Set[Method] = set()
begin: Pair = (0, 0)

for i in range(R):
    court[i] = list(input().strip())


def dfs(i: int, j: int, direction: int, cnt: int):
    global methods

    if cnt == K - 1:
        end = (i, j)
        methods.add((begin, end) if begin < end else (end, begin))
        return

    di, dj = directions[direction]
    ni = i + di
    nj = j + dj
    if ni >= R or nj >= R or ni < 0 or nj < 0 or court[ni][nj] == '#':
        return
    dfs(ni, nj, direction, cnt + 1)


for i in range(R):
    for j in range(C):
        if court[i][j] == '.':
            for direction in range(3):
                begin = (i, j)
                dfs(i, j, direction, 0)

print(methods.__len__())
