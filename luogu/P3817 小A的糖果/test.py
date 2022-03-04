# P3817 小A的糖果 https://www.luogu.com.cn/problem/P3817
# https://www.luogu.com.cn/record/70543761

N, X = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
if A[0] > X:
    diff = A[0] - X
    cnt += diff
    A[0] -= diff
for i in range(1, N):
    s = A[i - 1] + A[i]
    if s > X:
        diff = s - X
        cnt += diff
        A[i] -= diff
print(cnt)
