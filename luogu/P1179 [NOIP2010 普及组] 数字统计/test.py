# P1179 [NOIP2010 普及组] 数字统计 https://www.luogu.com.cn/problem/P1179

L, R = map(int, input().split())
print(sum(map(lambda x: str(x).count('2'), range(L, R + 1))))
