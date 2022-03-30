# P1138 第 k 小整数 https://www.luogu.com.cn/problem/P1138

N, K = map(int, input().split())
arr = sorted(map(int, input().split()))
cnt = 0
num = 0
for i in arr:
    if num != i:
        num = i
        cnt += 1
        if cnt == K:
            print(num)
            exit()
print('NO RESULT')
