# P1047 [NOIP2005 普及组] 校门外的树 https://www.luogu.com.cn/problem/P1047

l, m = map(int, input().split())
road = [1] * (l + 1)

for i in range(m):
    u, v = map(int, input().split())
    for j in range(u, v + 1):
        road[j] = 0

print(road.count(1))
