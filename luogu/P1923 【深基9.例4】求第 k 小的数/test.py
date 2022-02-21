# P1923 【深基9.例4】求第 k 小的数 https://www.luogu.com.cn/problem/P1923
# type: ignore

import numpy as np

N, K = map(int, input().split())
arr = np.fromstring(input(), dtype=np.uint32, sep=' ')
arr.sort()
print(arr[K])
