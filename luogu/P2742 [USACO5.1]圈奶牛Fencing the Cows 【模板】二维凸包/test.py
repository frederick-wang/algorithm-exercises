# P2742 [USACO5.1]圈奶牛Fencing the Cows 【模板】二维凸包

from collections import deque
from math import sqrt
from typing import Deque

N = int(input())
p = [tuple(map(float, input().split())) for _ in range(N)]
p.sort()

stk: Deque[int] = deque()


def get_distance(i: int) -> float:
    '''计算 stk[i] 和 stk[i - 1] 两点之间的距离

    Args:
        i (int): stk 中的第 i 个点

    Returns:
        float: stk 中第 i 个点与第 i - 1 个点之间的距离
    '''
    return sqrt((p[stk[i]][0] - p[stk[i - 1]][0])**2 +
                (p[stk[i]][1] - p[stk[i - 1]][1])**2)


def add_point(min_num: int, i: int):
    '''将 p[i] 添加到 stk 栈顶

    Args:
        min_num (int): stk 中最少要有的点数
        i (int): p 中的第 i 个点
    '''
    global p, stk
    # x1: p[stk[-1]][0] - p[stk[-2]][0]
    # y2: p[i][1] - p[stk[-1]][1]
    # y1: p[stk[-1]][1] - p[stk[-2]][1]
    # x2: p[i][0] - p[stk[-1]][0]
    while len(stk) > min_num and (p[stk[-1]][0] - p[stk[-2]][0]) * (
            p[i][1] - p[stk[-1]][1]) - (p[stk[-1]][1] - p[stk[-2]][1]) * (
                p[i][0] - p[stk[-1]][0]) <= 0:
        stk.pop()
    stk.append(i)


# 寻找下凸壳
for i in range(N):
    add_point(1, i)
# 寻找上凸壳
m = len(stk)
for i in range(N - 2, -1, -1):  # 注意这里结束是 0，会将 p[0] 第二次添加到 stk 栈顶，方便计算周长
    add_point(m, i)

if len(stk) == 2:  # 如果所有点是一条直线，stk 中只有两个 p[0]，直接计算首尾两点之间的距离再乘 2
    ans = 2 * sqrt((p[0][0] - p[-1][0])**2 + (p[0][1] - p[-1][1])**2)
else:
    ans = sum(map(get_distance, range(1, len(stk))))
print(f'{ans:.2f}')
