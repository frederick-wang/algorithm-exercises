# P5737 【深基7.例3】闰年展示 https://www.luogu.com.cn/problem/P5737

x, y = map(int, input().split())
years = tuple(
    i for i in range(x, y + 1) if i % 400 == 0 or (i % 100 != 0 and i % 4 == 0))
print(len(years))
print(*years)
