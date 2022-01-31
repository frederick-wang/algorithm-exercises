# P1909 [NOIP2016 普及组] 买铅笔 https://www.luogu.com.cn/problem/P1909

from math import ceil

n = int(input())

money_min = 100000001

for i in range(3):
    num, price = map(int, input().split())
    copies = ceil(n / num)
    money = copies * price
    if money < money_min:
        money_min = money

print(money_min)
