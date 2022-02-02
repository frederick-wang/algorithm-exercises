# P5724 【深基4.习5】求极差 / 最大跨度值 https://www.luogu.com.cn/problem/P5724

n = int(input())

a_min = 1000
a_max = 0

for a in map(int, input().split()):
    if a < a_min:
        a_min = a
    if a > a_max:
        a_max = a

print(a_max - a_min)
