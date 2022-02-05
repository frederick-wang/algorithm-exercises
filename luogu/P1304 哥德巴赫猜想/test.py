# P1304 哥德巴赫猜想 https://www.luogu.com.cn/problem/P1304

N = int(input())


def is_prime(n):  # type: (int) -> bool
    if n <= 1:
        return False
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


for i in range(4, N + 1, 2):
    a = 2
    b = i - 2
    if not is_prime(i - 2):
        j = 3
        for j in range(3, i // 2 + 1, 2):
            if is_prime(j) and is_prime(i - j):
                a, b = j, i - j
                break
    print('%d=%d+%d' % (i, a, b))
