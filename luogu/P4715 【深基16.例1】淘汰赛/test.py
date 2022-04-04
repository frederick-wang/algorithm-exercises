# P4715 【深基16.例1】淘汰赛 https://www.luogu.com.cn/problem/P4715

N = int(input())
s = list(map(int, input().split()))
HALF_LEN = 2**(N - 1)
l = max(s[:HALF_LEN])
r = max(s[HALF_LEN:])
print(s.index(r) + 1 if l > r else s.index(l) + 1)
