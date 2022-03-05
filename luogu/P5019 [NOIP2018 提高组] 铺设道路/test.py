# P5019 [NOIP2018 提高组] 铺设道路 https://www.luogu.com.cn/problem/P5019
# https://www.luogu.com.cn/record/70663442

N = int(input())
road = map(int, input().split())
prev = road.__next__()
day = prev
for d in road:
    if d > prev:
        day += d - prev
    prev = d
print(day)
