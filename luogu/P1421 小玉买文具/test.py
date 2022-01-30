# P1421 小玉买文具 https://www.luogu.com.cn/problem/P1421

a, b = map(int, input().split())

money = a * 10 + b
num = money // 19
print(num)
