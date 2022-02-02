# P1420 最长连号 https://www.luogu.com.cn/problem/P1420

n = int(input())

a = list(map(int, input().split()))

consecutive_count = 1
max_consecutive_count = 1

for i in range(n - 1):
    if a[i] + 1 == a[i + 1]:
        consecutive_count += 1
    else:
        if max_consecutive_count < consecutive_count:
            max_consecutive_count = consecutive_count
        consecutive_count = 1

print(max(max_consecutive_count, consecutive_count))
