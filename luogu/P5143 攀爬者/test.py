# P5143 攀爬者 https://www.luogu.com.cn/problem/P5143

from typing import List, Tuple

N = int(input())

sum = 0.0
points: List[Tuple[int, int, int]] = []

for i in range(N):
    x, y, z = map(int, input().split())
    points.append((x, y, z))

points = sorted(points, key=lambda x: x[2])

for i in range(1, N):
    distance = ((points[i][0] - points[i - 1][0])**2 +
                (points[i][1] - points[i - 1][1])**2 +
                (points[i][2] - points[i - 1][2])**2)**0.5
    sum += distance

print('%.3f' % sum)
