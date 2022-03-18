# P1433 吃奶酪 https://www.luogu.com.cn/problem/P1433
# 用 PyPy3 提交，否则会 TLE
# https://www.luogu.com.cn/record/71706352

from math import sqrt

N = int(input())

p = [tuple(map(float, input().split())) for _ in range(N)]  # 各个点的坐标
# d[i][route] 表示从索引为 i 的点出发，路线为 route 时的最小距离
d = [[float('inf')] * (1 << N) for _ in range(N)]
min_distance = float('inf')  # 吃掉所有奶酪的最小距离


def dis(x1: float, y1: float, x2: float, y2: float):
    '''计算两点之间的距离'''
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)


for r in range(1, 1 << N):
    for i in range(N):
        ib = 1 << i
        if r & ib:  # 即为 r & ib != 0，也就是说第 i 个点在路线 r 中
            if r == ib:  # 如果当前点为出发点，则距离为 0
                d[i][r] = 0
            else:
                for j in range(N):
                    if i != j and r & (1 << j):  # j 点和 i 点相异，并且 j 点也在路线 r 中
                        d[i][r] = min(d[i][r], d[j][r - ib] + dis(*p[i], *p[j]))
        if r == (1 << N) - 1:  # 如果全部点都已在路线中，则更新最小距离
            min_distance = min(min_distance, d[i][r] + dis(0, 0, *p[i]))
print('%.2f' % min_distance)
