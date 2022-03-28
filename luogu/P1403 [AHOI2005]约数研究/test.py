# P1403 [AHOI2005]约数研究 https://www.luogu.com.cn/problem/P1403

N = int(input())
print(sum(N // i for i in range(1, N + 1)))
