# P8225 「Wdoi-5」天才⑨与天才拆分 https://www.luogu.com.cn/problem/P8225

pow10 = tuple(10**k for k in range(11))
T = int(input())
for _ in range(T):
    k, n = map(int, input().split())
    print('baka' if n % (pow10[k] - 1) else 'aya')
