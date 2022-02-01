# P1980 [NOIP2013 普及组] 计数问题 https://www.luogu.com.cn/problem/P1980

raw_input = input().split()
n = int(raw_input[0])
x = raw_input[1]

s = 0
for i in map(str, range(1, n + 1)):
    s += i.count(x)

print(s)
