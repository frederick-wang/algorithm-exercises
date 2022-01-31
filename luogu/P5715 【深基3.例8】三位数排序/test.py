# P5715 【深基3.例8】三位数排序 https://www.luogu.com.cn/problem/P5715

a, b, c = map(int, input().split())

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print(a, b, c)
