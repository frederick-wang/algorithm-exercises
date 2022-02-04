# P5015 [NOIP2018 普及组] 标题统计 https://www.luogu.com.cn/problem/P5015

from curses.ascii import isalnum

print(len(tuple(filter(isalnum, input()))))
