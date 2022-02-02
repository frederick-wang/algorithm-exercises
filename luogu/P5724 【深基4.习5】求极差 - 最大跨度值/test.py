# P5724 【深基4.习5】求极差 / 最大跨度值 https://www.luogu.com.cn/problem/P5724

n = int(input())
A = list(map(int, input().split()))

print(max(A) - min(A))
