# P1208 [USACO1.3]混合牛奶 Mixing Milk https://www.luogu.com.cn/problem/P1208
# https://www.luogu.com.cn/record/70644027

n, m = map(int, input().split())
farmers = sorted([tuple(map(int, input().split())) for _ in range(m)])
cost = 0
for p, a in farmers:
    if n >= a:
        n -= a
        cost += p * a
    else:
        cost += p * n
        break
print(cost)
