# P1223 排队接水 https://www.luogu.com.cn/problem/P1223
# https://www.luogu.com.cn/record/70524322

N = int(input())
T = list(map(int, input().split()))
result = sorted((T[i], i + 1) for i in range(N))
print(*map(lambda x: x[1], result))
avg_time = 0
for i in range(N):
    avg_time += result[i][0] * (N - i - 1)
print('%.2f' % (avg_time / N))
