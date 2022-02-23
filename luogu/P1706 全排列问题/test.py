# P1706 全排列问题 https://www.luogu.com.cn/problem/P1706

from itertools import permutations

N = int(input())
templ = '% 5d' * N
print('\n'.join(map(lambda x: templ % x, permutations(range(1, N + 1)))))
