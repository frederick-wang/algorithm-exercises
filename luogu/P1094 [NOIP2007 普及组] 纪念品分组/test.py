# P1094 [NOIP2007 普及组] 纪念品分组 https://www.luogu.com.cn/problem/P1094
# https://www.luogu.com.cn/record/70577371

W = int(input())
N = int(input())
P = sorted([int(input()) for _ in range(N)])
i = 0
j = N - 1
cnt = 0
while i <= j:
    if P[i] + P[j] <= W:
        i += 1
        j -= 1
    else:
        j -= 1
    cnt += 1
print(cnt)
