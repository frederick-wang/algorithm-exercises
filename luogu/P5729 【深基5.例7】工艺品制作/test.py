# P5729 【深基5.例7】工艺品制作 https://www.luogu.com.cn/problem/P5729

w, x, h = map(int, input().split())
v = [[[1] * h for _ in range(x)] for _ in range(w)]

q = int(input())

result = 0
for _ in range(q):
    x_1, y_1, z_1, x_2, y_2, z_2 = map(int, input().split())
    for i in range(x_1 - 1, x_2):
        for j in range(y_1 - 1, y_2):
            for k in range(z_1 - 1, z_2):
                v[i][j][k] = 0

for i in range(w):
    for j in range(x):
        for k in range(h):
            if v[i][j][k]:
                result += 1

print(result)
