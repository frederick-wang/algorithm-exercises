# P1657 选书 https://www.luogu.com.cn/problem/P1657

X = int(input())
wants = [list(map(int, input().split())) for _ in range(X)]
books = [0] * (X + 1)
ans = 0


def dfs(i: int):
    global ans
    if i == X:
        ans += 1
        return
    for j in wants[i]:
        if not books[j]:
            books[j] = 1
            dfs(i + 1)
            books[j] = 0


dfs(0)
print(ans)
