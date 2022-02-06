# P1563 [NOIP2016 提高组] 玩具谜题 https://www.luogu.com.cn/problem/P1563

from typing import List, Tuple

if __name__ == '__main__':
    n, m = map(int, input().split())
    toys: List[Tuple[int, str]] = []

    for _ in range(n):
        raw = input().split()
        orientation = int(raw[0])  # 0 表示朝向圈内，1 表示朝向圈外
        occupation = raw[1]
        toys.append((orientation, occupation))

    idx = 0
    for _ in range(m):
        # 若 a=0，表示向左数 s 个人；若 a=1，表示向右数 s 个人
        a, s = map(int, input().split())
        delta = (-s if a else s) if toys[idx][0] else (s if a else -s)
        if idx + delta < 0:
            idx = n + idx + delta
        elif idx + delta >= n:
            idx = idx + delta - n
        else:
            idx += delta

    print(toys[idx][1])
