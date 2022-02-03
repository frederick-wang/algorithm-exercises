# P1789 【Mc生存】插火把 https://www.luogu.com.cn/problem/P1789

n, m, k = map(int, input().split())

s = [0] * n**2


def idx(x, y):  # type: (int, int) -> int
    return (0 if x < 0 else
            (n - 1) if x > n - 1 else x) * n + (0 if y < 0 else
                                                (n - 1) if y > n - 1 else y)


for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for i in range(x - 2, x + 3):
        s[idx(i, y)] = 1
    for i in range(y - 2, y + 3):
        s[idx(x, i)] = 1
    s[idx(x - 1, y - 1)] = 1
    s[idx(x - 1, y + 1)] = 1
    s[idx(x + 1, y - 1)] = 1
    s[idx(x + 1, y + 1)] = 1

for _ in range(k):
    o, p = map(int, input().split())
    o -= 1
    p -= 1
    for i in range(o - 2, o + 3):
        for j in range(p - 2, p + 3):
            s[idx(i, j)] = 1

print(s.count(0))
