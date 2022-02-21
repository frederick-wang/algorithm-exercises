# P1012 [NOIP1998 提高组] 拼数 https://www.luogu.com.cn/problem/P1012

from functools import cmp_to_key

N = int(input())
nums = input().split()


def cmp(a: str, b: str):
    ab = a + b
    ba = b + a
    if ab > ba:
        return -1
    if ab < ba:
        return 1
    return 0


nums.sort(key=cmp_to_key(cmp))
print(''.join(nums))
