# P1478 陶陶摘苹果（升级版） https://www.luogu.com.cn/problem/P1478
# https://www.luogu.com.cn/record/70548629

N, s = map(int, input().split())
A, B = map(int, input().split())
H = A + B
apples = filter(
    lambda x: H >= x[0],
    sorted([tuple(map(int,
                      input().split())) for _ in range(N)],
           key=lambda x: x[1]))
cnt = 0
for x, y in apples:
    if s >= y:
        s -= y
        cnt += 1
    else:
        break
print(cnt)
