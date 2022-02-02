# P1423 小玉在游泳 https://www.luogu.com.cn/problem/P1423

x = float(input())

step = 2.0
s = 0.0
n = 0

while s < x:
    s += step
    n += 1
    step *= 0.98

print(n)
