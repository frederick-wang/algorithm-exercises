# P1424 小鱼的航程(改进版) https://www.luogu.com.cn/problem/P1424

x, n = map(int, input().split())

ans = 0
while n:
    if 1 <= x <= 5:
        ans += 250
    x = x + 1 if x < 7 else 1
    n -= 1

print(ans)
