# P2670 [NOIP2015 普及组] 扫雷游戏 https://www.luogu.com.cn/problem/P2670

from typing import List

n, m = map(int, input().split())

board: List[str] = []
for _ in range(n):
    board.append(input().strip())


def calc_mine_num(x: int, y: int) -> int:
    return sum(row[y - 1 if y - 1 >= 0 else 0:y + 2].count('*')
               for row in board[x - 1 if x - 1 >= 0 else 0:x + 2])


for i in range(n):
    for j in range(m):
        if board[i][j] == '*':
            print('*', end='')
        else:
            print(calc_mine_num(i, j), end='')
    print()
