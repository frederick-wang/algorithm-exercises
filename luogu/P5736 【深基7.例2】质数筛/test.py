# P5736 【深基7.例2】质数筛 https://www.luogu.com.cn/problem/P5736

from array import array

n = int(input())
nums = tuple(map(int, input().split()))
max_num = max(nums)

T = array('b', [1]) * (max_num + 1)
T[0] = 0
T[1] = 0
for i in range(4, max_num + 1, 2):
    T[i] = 0
i = 3
while i**2 <= max_num:
    if T[i]:
        for j in range(i**2, max_num + 1, i):
            T[j] = 0
    i += 2
print(*filter(T.__getitem__, nums))
