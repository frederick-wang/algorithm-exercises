# P1036 [NOIP2002 普及组] 选数 https://www.luogu.com.cn/problem/P1036

from itertools import combinations

N, K = map(int, input().split())
nums = list(map(int, input().split()))


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if not n % 2:
        return False
    i = 3
    while i * i <= n:
        if not n % i:
            return False
        i += 2
    return True


result = 0
for com in combinations(nums, K):
    if is_prime(s := sum(com)):
        result += 1

print(result)
