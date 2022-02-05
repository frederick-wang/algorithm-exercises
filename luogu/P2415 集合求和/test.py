# P2415 集合求和 https://www.luogu.com.cn/problem/P2415

s = list(map(int, input().split()))
n = 2**len(s) // 2
print(sum(map(lambda x: x * n, s)))
