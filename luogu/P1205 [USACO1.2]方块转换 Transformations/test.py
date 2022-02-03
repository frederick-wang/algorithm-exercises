# P1205 [USACO1.2]方块转换 Transformations https://www.luogu.com.cn/problem/P1205

from typing import List

N = int(input())
s_init = []  # type: List[str]
s_final = []  # type: List[str]

for _ in range(N):
    s_init.append(input().strip())

for _ in range(N):
    s_final.append(input().strip())


def is_eq(s1, s2):  # type: (List[str], List[str]) -> bool
    for i, line in enumerate(s1):
        if line != s2[i]:
            return False
    return True


def rotate_90(s1):  # type: (List[str]) -> List[str]
    s_new = [''] * N
    for i in range(N):
        for j in range(N):
            s_new[i] += s1[N - j - 1][i]
    return s_new


def rotate_180(s1):  # type: (List[str]) -> List[str]
    s_new = [''] * N
    for i in range(N):
        for j in range(N):
            s_new[i] += s1[N - i - 1][N - j - 1]
    return s_new


def rotate_270(s1):  # type: (List[str]) -> List[str]
    s_new = [''] * N
    for i in range(N):
        for j in range(N):
            s_new[i] += s1[j][N - i - 1]
    return s_new


def reflect(s1):  # type: (List[str]) -> List[str]
    return [line[::-1] for line in s1]


# 转 90°
if is_eq(rotate_90(s_init), s_final):
    print(1)
    exit()
# 转 180°
if is_eq(rotate_180(s_init), s_final):
    print(2)
    exit()
# 转 270°
if is_eq(rotate_270(s_init), s_final):
    print(3)
    exit()
# 反射
if is_eq(reflect(s_init), s_final):
    print(4)
    exit()
# 组合
if is_eq(rotate_90(reflect(s_init)), s_final) or is_eq(
        rotate_180(reflect(s_init)), s_final) or is_eq(
            rotate_270(reflect(s_init)), s_final):
    print(5)
    exit()
# 不改变
if is_eq(s_init, s_final):
    print(6)
    exit()

print(7)
