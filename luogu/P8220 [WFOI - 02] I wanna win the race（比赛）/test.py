# P8220 [WFOI - 02] I wanna win the race（比赛） https://www.luogu.com.cn/problem/P8220

N = int(input())
A, B, C = map(int, input().split())
if C < N:
    print(2 * N - 1)
else:
    print(min(2 * N + B - A, 2 * C + 1))
