# P1425 小鱼的游泳时间 https://www.luogu.com.cn/problem/P1425
a, b, c, d = map(int, input().split())

duration_hours = c - a
duration_minutes = d - b
duration = duration_hours * 60 + duration_minutes

hours = duration // 60
minutes = duration % 60
print(hours, minutes)
