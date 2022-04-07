# P1887 乘积最大3 https://www.luogu.com.cn/problem/P1887

N, M = map(int, input().split())
d, m = divmod(N, M)
nums = [d] * (M - m) + [d + 1] * m
print(' '.join(map(str, nums)))
