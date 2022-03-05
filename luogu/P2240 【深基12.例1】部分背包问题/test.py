# P2240 【深基12.例1】部分背包问题 https://www.luogu.com.cn/problem/P2240

N, t = map(int, input().split())
gold = sorted([tuple(map(int,
                         input().split())) for _ in range(N)],
              key=lambda x: -x[1] / x[0])
val = 0.0
for m, v in gold:
    if t >= m:
        t -= m
        val += v
    else:
        val += v * t / m
        break
print('%.2f' % val)
