# P1567 统计天数 https://www.luogu.com.cn/problem/P1567

N = int(input())

temperatures = tuple(map(int, input().split()))

s = 1
max_s = 1

for i in range(1, N):
    if temperatures[i] > temperatures[i - 1]:
        s += 1
        if s > max_s:
            max_s = s
    else:
        s = 1

print(max_s)
