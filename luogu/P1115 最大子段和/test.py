# P1115 最大子段和 https://www.luogu.com.cn/problem/P1115

N = int(input())
a = list(map(int, input().split()))
s = a[0]
max_s = int(-1e10)
for i in range(1, N):
    s = max(s + a[i], a[i])
    max_s = max(max_s, s)
print(max_s)
