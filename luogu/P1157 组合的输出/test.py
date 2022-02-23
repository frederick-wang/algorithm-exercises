# P1157 组合的输出 https://www.luogu.com.cn/problem/P1157

from itertools import combinations

N, R = map(int, input().split())

print('\n'.join(
    map(lambda x: ''.join(map('{: 3d}'.format, x)),
        combinations(range(1, N + 1), R))))
