# P1551 亲戚 https://www.luogu.com.cn/problem/P1551
# 并查集，使用了「启发式合并」与「路径压缩」，详见 https://oi-wiki.org/ds/dsu/

N, M, P = map(int, input().split())

# 子树大小记录
tree_size = [1] * (N + 1)
fa = [i for i in range(N + 1)]


def find(x: int) -> int:
    if x != fa[x]:
        fa[x] = find(fa[x])
    return fa[x]


for _ in range(M):
    x, y = map(int, input().split())
    x = find(x)
    y = find(y)
    # 启发式合并
    if x != y:
        # 保证 x <= y
        if tree_size[x] > tree_size[y]:
            x, y = y, x
        fa[x] = y
        # 只需要更新根节点的子树大小，子节点的子树大小不会再被用到了，因而不用更新
        tree_size[y] += tree_size[x]

for _ in range(P):
    x, y = map(int, input().split())
    print('Yes' if find(x) == find(y) else 'No')
