# P1918 保龄球 https://www.luogu.com.cn/problem/P1918

N = int(input())
d = {a_i: i for i, a_i in enumerate(input().split(), 1)}
Q = int(input())
print('\n'.join(map(str, map(lambda _: d.get(input().strip(), 0), range(Q)))))
