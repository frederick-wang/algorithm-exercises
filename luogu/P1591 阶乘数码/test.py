# P1591 阶乘数码 https://www.luogu.com.cn/problem/P1591

t = int(input())

factorials = [0] * 1001
factorials[0] = 1


def factorial(n: int) -> int:
    if factorials[n]:
        return factorials[n]
    return n * factorial(n - 1)


for _ in range(t):
    raw = input().strip().split()
    n = int(raw[0])
    a = raw[1]
    print(str(factorial(n)).count(a))
