# P1255 数楼梯 https://www.luogu.com.cn/problem/P1255
# https://www.luogu.com.cn/record/70277153

N = int(input())
record = [0] * (N + 1)
if N > 0:
    record[1] = 1
if N > 1:
    record[2] = 2
for i in range(3, N + 1):
    record[i] = record[i - 1] + record[i - 2]
print(record[N])
