# P1190 [NOIP2010 普及组] 接水问题 https://www.luogu.com.cn/problem/P1190

from collections import deque

n, M = map(int, input().split())
w = deque(map(int, input().split()))
taps = [0] * M
ans = 0

while n:
    for i in range(M):
        if not taps[i]:
            if len(w):
                taps[i] = w.popleft()
            else:
                print(ans + max(taps))
                exit()
    min_val = min(taps)
    ans += min_val
    for i in range(M):
        taps[i] -= min_val
        if not taps[i]:
            n -= 1
print(ans)
