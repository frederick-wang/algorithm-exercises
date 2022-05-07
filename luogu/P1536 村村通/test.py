# P1536 村村通 https://www.luogu.com.cn/problem/P1536

fa = [0] * 1001


def find(x: int) -> int:
    if x != fa[x]:
        fa[x] = find(fa[x])
    return fa[x]


while True:
    raw_input = input().strip()
    if raw_input == '0':
        exit()
    N, M = map(int, raw_input.split())
    fa[:N + 1] = range(N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        fa[find(a)] = find(b)
    print(sum(i == fa[i] for i in range(1, N + 1)) - 1)
