# P2089 烤鸡 https://www.luogu.com.cn/problem/P2089

from itertools import product

N = int(input())
result = list(
    map(lambda x: ' '.join(map(str, x)),
        filter(lambda x: sum(x) == N, product((1, 2, 3), repeat=10))))
print(len(result))
print('\n'.join(result))
