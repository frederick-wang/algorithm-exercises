# P5707 【深基2.例12】上学迟到 https://www.luogu.com.cn/problem/P5707

from math import ceil

s, v = map(int, input().split())

d_mins = ceil(s / v) + 10
result = 8 * 60 - d_mins if d_mins <= 8 * 60 else 24 * 60 - (d_mins - 8 * 60)
hours = result // 60
mins = result % 60
print('{:02d}:{:02d}'.format(hours, mins))
