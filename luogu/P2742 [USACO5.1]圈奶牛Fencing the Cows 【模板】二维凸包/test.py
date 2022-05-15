# P2742 [USACO5.1]圈奶牛Fencing the Cows 【模板】二维凸包

from collections import deque
from math import sqrt
from typing import Deque, Tuple

N = int(input())
p = [tuple(map(float, input().split())) for _ in range(N)]
p.sort()

stk: Deque[Tuple[float, float]] = deque()


def distance(A: Tuple[float, float], B: Tuple[float, float]) -> float:
    '''计算两点之间的距离

    Args:
        A (Tuple[float, float]): 第一个点
        B (Tuple[float, float]): 第二个点

    Returns:
        float: 两点之间的距离
    '''
    return sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)


def i_distance(i: int) -> float:
    '''计算 stk[i] 和 stk[i - 1] 两点之间的距离

    Args:
        i (int): stk 中的第 i 个点

    Returns:
        float: stk 中第 i 个点与第 i - 1 个点之间的距离
    '''
    return distance(stk[i], stk[i - 1])


def cross_product(A: Tuple[float, float], B: Tuple[float, float],
                  C: Tuple[float, float]) -> float:
    r'''计算 \overrightarrow{AB} \times \overrightarrow{BC} 的叉积

    Args:
        A (Tuple[float, float]): 第一个点
        B (Tuple[float, float]): 第二个点
        C (Tuple[float, float]): 第三个点

    Returns:
        float: 向量叉积
    '''
    return (B[0] - A[0]) * (C[1] - B[1]) - (B[1] - A[1]) * (C[0] - B[0])


def add_point(min_num: int, point: Tuple[float, float]):
    '''将 point 添加到 stk 栈顶

    Args:
        min_num (int): stk 中最少要有的点数
        i (Tuple[float, float]): 待添加点
    '''
    global p, stk
    while len(stk) > min_num and cross_product(stk[-2], stk[-1], point) <= 0:
        stk.pop()
    stk.append(point)


# 寻找下凸壳
for point in p:
    add_point(1, point)
# 寻找上凸壳
m = len(stk)
for i in range(N - 2, -1, -1):  # 注意这里结束是 0，会将 p[0] 第二次添加到 stk 栈顶，方便计算周长
    add_point(m, p[i])

if len(stk) == 2:  # 如果所有点是一条直线，stk 中只有两个 p[0]，直接计算首尾两点之间的距离再乘 2
    ans = 2 * distance(stk[0], stk[-1])
else:
    ans = sum(map(i_distance, range(1, len(stk))))
print(f'{ans:.2f}')
