# P5723 【深基4.例13】质数口袋 https://www.luogu.com.cn/problem/P5723


def is_prime(n):  # type: (int) -> bool
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


L = int(input())
s = 0
num = 0

if 2 <= L:
    print(2)
    s += 2
    num += 1

n = 3
while True:
    if is_prime(n):
        s += n
        if s > L:
            break
        print(n)
        num += 1
    n += 2

print(num)
