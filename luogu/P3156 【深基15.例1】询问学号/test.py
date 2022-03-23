# P3156 【深基15.例1】询问学号 https://www.luogu.com.cn/problem/P3156

import numpy as np

N, M = map(int, input().split())
stu = np.fromstring(input(), dtype=np.uint32, sep=' ', count=N)
print('\n'.join(map(lambda x: str(stu[x - 1]), map(int, input().split()))))
