# P5708 【深基2.习2】三角形面积 https://www.luogu.com.cn/problem/P5708

from math import sqrt

a, b, c = map(float, input().split())

p = 1 / 2 * (a + b + c)
s = sqrt(p * (p - a) * (p - b) * (p - c))

print('%.1f' % s)
