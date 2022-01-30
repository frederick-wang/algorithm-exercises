# P5709 【深基2.习6】Apples Prologue / 苹果和虫子 https://www.luogu.com.cn/problem/P5709

from math import ceil

m, t, s = map(int, input().split())
if t == 0:
    print(0)
else:
    eaten = ceil(s / t)
    if eaten <= m:
        print(m - eaten)
    else:
        print(0)
