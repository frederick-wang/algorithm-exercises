# P1035 [NOIP2002 普及组] 级数求和 https://www.luogu.com.cn/problem/P1035

k = int(input())

n = 1
s = 0.0

while True:
    s += 1.0 / n
    if s > k:
        break
    n += 1

print(n)
