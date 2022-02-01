# P2669 [NOIP2015 普及组] 金币 https://www.luogu.com.cn/problem/P2669

k = int(input())

n = 1
i = 0
s = 0

while k:
    s += n
    i += 1
    if i == n:
        i = 0
        n += 1
    k -= 1

print(s)
