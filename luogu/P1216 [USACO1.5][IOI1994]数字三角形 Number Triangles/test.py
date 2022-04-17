# P1216 [USACO1.5][IOI1994]数字三角形 Number Triangles https://www.luogu.com.cn/problem/P1216

R = int(input())
nums = [list(map(int, input().split())) for _ in range(R)]
d = [[0] * i for i in range(1, R + 1)]
d[0][0] = nums[0][0]
for i in range(1, R):
    d[i][0] = d[i - 1][0] + nums[i][0]
    d[i][i] = d[i - 1][i - 1] + nums[i][i]
    for j in range(1, i):
        d[i][j] = max(d[i - 1][j - 1], d[i - 1][j]) + nums[i][j]
print(max(d[R - 1]))
