# P5743 【深基7.习8】猴子吃桃 https://www.luogu.com.cn/problem/P5743

n = int(input())

num = 1
for _ in range(n - 1):
    num = (num + 1) * 2
print(num)
