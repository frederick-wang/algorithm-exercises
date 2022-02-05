# P5739 【深基7.例7】计算阶乘 https://www.luogu.com.cn/problem/P5739


def factorial(n):  # type: (int) -> int
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(int(input())))
