# P1990 覆盖墙壁 https://www.luogu.com.cn/problem/P1990
# https://www.luogu.com.cn/record/70383925

from array import array

N = int(input())
result = array('I', [0]) * max(3, (N + 1))
result[0] = 1
result[1] = 1
result[2] = 2
for i in range(3, N + 1):
    result[i] = (2 * result[i - 1] + result[i - 3]) % 10000
print(result[N])
