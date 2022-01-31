# P4414 [COCI2006-2007#2] ABC https://www.luogu.com.cn/problem/P4414

A, B, C = sorted(map(int, input().split()))
order = input()

d = {'A': A, 'B': B, 'C': C}

print(d[order[0]], d[order[1]], d[order[2]])
