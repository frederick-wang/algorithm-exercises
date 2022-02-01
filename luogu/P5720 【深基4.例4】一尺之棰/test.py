# P5720 【深基4.例4】一尺之棰 https://www.luogu.com.cn/problem/P5720

a = int(input())

day = 1

while a > 1:
    a //= 2
    day += 1

print(day)
